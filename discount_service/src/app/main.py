from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Discount service")


class DiscountRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    promocode: str | None = None


class DiscountResponse(BaseModel):
    discount_percent: float
    reason: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "discount-service"}


@app.post("/discounts/calculate", response_model=DiscountResponse)
def calculate_discount(request: DiscountRequest) -> DiscountResponse:
    if request.promocode == "STUDENT10":
        return DiscountResponse(
            discount_percent=10.0,
            reason="Because of promocode STUDENT10",
        )
    if request.promocode == "ISU80":
        return DiscountResponse(
            discount_percent=80.0,
            reason="Because of promocode ISU80",
        )
    if request.quantity >= 10:
        return DiscountResponse(
            discount_percent=5.0,
            reason="Because of large quantity >= 10",
        )
    return DiscountResponse(
        discount_percent=0.0,
        reason="No discount",
    )
