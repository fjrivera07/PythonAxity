from fastapi import FastAPI

from laboratorio_fastapi.routers import auth, order, user

app = FastAPI(title="Orders API")

app.include_router(user.router)
app.include_router(order.router)
app.include_router(auth.router)
