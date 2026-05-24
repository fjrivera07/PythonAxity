from fastapi import FastAPI

from orders_service.api.routers import auth, orders, users
from orders_service.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


# app.include_router(health.router)
app.include_router(auth.router)
app.include_router(orders.router)
app.include_router(users.router)
