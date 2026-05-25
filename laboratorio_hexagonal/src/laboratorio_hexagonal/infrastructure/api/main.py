from fastapi import FastAPI

from ...application.dto import CreateOrderRequest
from ...application.use_cases import CreateOrderUseCase
from ..notifications.http_notifier import HttpNotifier
from ..repositories.memory import InMemoryOrderRepository

app = FastAPI(title="Hexagonal Orders API")


# Dependency wiring (manual DI)
def get_use_case() -> CreateOrderUseCase:
    repository = InMemoryOrderRepository()
    notifier = HttpNotifier(endpoint="https://example.com/notify")

    return CreateOrderUseCase(repository=repository, notifier=notifier)


@app.post("/orders")
def create_order(request: CreateOrderRequest):
    use_case = get_use_case()

    response = use_case.execute(request)

    return response
