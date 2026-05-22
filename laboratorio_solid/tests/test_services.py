from laboratorio_solid.application.services import OrderService
from laboratorio_solid.infrastructure.memory_repository import MemoryOrderRepository


def test_create_order():

    repo = MemoryOrderRepository()
    service = OrderService(repo)

    order = service.create_order(1, "Juan", 150.0)

    assert order.id == 1
    assert order.customer_name == "Juan"
    assert order.total == 150.0
