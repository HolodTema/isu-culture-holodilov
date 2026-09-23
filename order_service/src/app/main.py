from contextlib import asynccontextmanager
from datetime import datetime

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .database import get_order, init_db, save_order
from .settings import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    init_db(settings.database_url)
    app.state.settings = settings
    yield


app = FastAPI(title="Order Service", lifespan=lifespan)


class OrderRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    promocode: str | None = None


class OrderResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    subtotal: float
    discount_percent: float
    discount_amount: float
    total: float
    discount_reason: str


class StoredOrderResponse(BaseModel):
    id: int
    product_id: str
    quantity: int
    unit_price: float
    subtotal: float
    discount_percent: float
    discount_amount: float
    total: float
    created_at: datetime


class ProductFromService(BaseModel):
    id: str
    name: str
    price: float
    available: bool


class DiscountFromService(BaseModel):
    discount_percent: float
    reason: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "order-service"}


@app.post("/orders", response_model=OrderResponse)
async def create_order(order: OrderRequest) -> OrderResponse:
    settings = app.state.settings

    product = await fetch_product(settings.product_service_url, order.product_id)

    if not product.available:
        raise HTTPException(
            status_code=400,
            detail=f"Product '{order.product_id}' is not available",
        )

    discount = await fetch_discount(
        settings.discount_service_url,
        product_id=product.id,
        quantity=order.quantity,
        unit_price=product.price,
        promocode=order.promocode,
    )

    subtotal = round(product.price * order.quantity, 2)
    discount_amount = round(subtotal * discount.discount_percent / 100, 2)
    total = round(subtotal - discount_amount, 2)

    save_order(
        {
            "product_id": product.id,
            "quantity": order.quantity,
            "unit_price": product.price,
            "subtotal": subtotal,
            "discount_percent": discount.discount_percent,
            "discount_amount": discount_amount,
            "total": total,
        }
    )

    return OrderResponse(
        product_id=product.id,
        quantity=order.quantity,
        unit_price=product.price,
        subtotal=subtotal,
        discount_percent=discount.discount_percent,
        discount_amount=discount_amount,
        total=total,
        discount_reason=discount.reason,
    )


@app.get("/orders/{order_id}", response_model=StoredOrderResponse)
def read_order(order_id: int) -> StoredOrderResponse:
    saved = get_order(order_id)

    if saved is None:
        raise HTTPException(
            status_code=404,
            detail=f"Order '{order_id}' was not found",
        )

    return StoredOrderResponse(
        id=saved["id"],
        product_id=saved["product_id"],
        quantity=saved["quantity"],
        unit_price=float(saved["unit_price"]),
        subtotal=float(saved["subtotal"]),
        discount_percent=float(saved["discount_percent"]),
        discount_amount=float(saved["discount_amount"]),
        total=float(saved["total"]),
        created_at=saved["created_at"],
    )


async def fetch_product(base_url: str, product_id: str) -> ProductFromService:
    url = f"{base_url}/products/{product_id}"

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.get(url)
    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Product service is unavailable: {exc}",
        ) from exc

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=f"Product '{product_id}' was not found",
        )

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail="Product service returned an unexpected error",
        )

    return ProductFromService.model_validate(response.json())


async def fetch_discount(
    base_url: str,
    product_id: str,
    quantity: int,
    unit_price: float,
    promocode: str | None,
) -> DiscountFromService:
    url = f"{base_url}/discounts/calculate"
    payload = {
        "product_id": product_id,
        "quantity": quantity,
        "unit_price": unit_price,
        "promocode": promocode,
    }

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.post(url, json=payload)
    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Discount service is unavailable: {exc}",
        ) from exc

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail="Discount service returned an unexpected error",
        )

    return DiscountFromService.model_validate(response.json())
