from laboratorio_solid.application.services import OrderService
from laboratorio_solid.infrastructure.memory_repository import MemoryOrderRepository


def test_list_orders():

    repo = MemoryOrderRepository()
    service = OrderService(repo)

    service.create_order(1, "Juan", 100.0)
    service.create_order(2, "Maria", 200.0)

    orders = service.list_orders()

    assert len(orders) == 2
