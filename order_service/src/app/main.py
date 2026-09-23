import os
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="Order Service")


PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL",
    "http://127.0.0.1:8001",
)


DISCOUNT_SERVICE_URL = os.getenv(
    "DISCOUNT_SERVICE_URL",
    "http://127.0.0.1:8003",
)


class OrderRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    promocode: str | None = None


class OrderResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    cost_before_discount: float
    discount_percent: float
    discount_cost: float
    cost_after_discount: float


class ProductFromService(BaseModel):
    id: str
    name: str
    price: float
    available: bool


class CalculateDiscountRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    promocode: str | None = None


class CalculateDiscountResponse(BaseModel):
    discount_percent: float
    reason: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "order-service"}


@app.post("/orders", response_model=OrderResponse)
async def create_order(order: OrderRequest) -> OrderResponse:
    product = await fetch_product(order.product_id)
    if not product.available:
        raise HTTPException(
            status_code=400,
            detail=f"Product '{order.product_id}' is not available",
        )
    cost_before_discount = product.price * order.quantity
    calculate_discount_request = CalculateDiscountRequest(
        product_id=product.id,
        quantity=order.quantity,
        unit_price=product.price,
        promocode=order.promocode,
    )
    calculate_discount_response = await fetch_discount(calculate_discount_request)
    discount_cost = cost_before_discount / 100.0 * calculate_discount_response.discount_percent
    cost_after_discount = cost_before_discount - discount_cost
    return OrderResponse(
        product_id=product.id,
        quantity=order.quantity,
        unit_price=product.price,
        cost_before_discount=cost_before_discount,
        discount_percent=calculate_discount_response.discount_percent,
        discount_cost=discount_cost,
        cost_after_discount=cost_after_discount,
    )


async def fetch_product(product_id: str) -> ProductFromService:
    url = f"{PRODUCT_SERVICE_URL}/products/{product_id}"
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


async def fetch_discount(calculate_discount_request: CalculateDiscountRequest) -> CalculateDiscountResponse:
    url = f"{DISCOUNT_SERVICE_URL}/discounts/calculate"
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.post(
                url,
                json=calculate_discount_request.model_dump(),
            )
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
    return CalculateDiscountResponse.model_validate(response.json())
