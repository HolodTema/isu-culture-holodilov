import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    product_service_url: str
    discount_service_url: str
    database_url: str


def get_settings() -> Settings:
    names = (
        "PRODUCT_SERVICE_URL",
        "DISCOUNT_SERVICE_URL",
        "DATABASE_URL",
    )
    list_missed_env = [name for name in names if not os.getenv(name)]
    if list_missed_env:
        raise RuntimeError(
            "Missing required environment variables: " + " ".join(list_missed_env)
    return Settings(
        product_service_url=os.environ["PRODUCT_SERVICE_URL"],
        discount_service_url=os.environ["DISCOUNT_SERVICE_URL"],
        database_url=os.environ["DATABASE_URL"],
    )


