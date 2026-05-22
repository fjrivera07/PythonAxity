import pytest

from laboratorio_solid.application.services import OrderService
from laboratorio_solid.infrastructure.memory_repository import MemoryOrderRepository
from laboratorio_solid.infrastructure.sql_repository import SqlOrderRepository


@pytest.mark.parametrize(
    "repository",
    [
        MemoryOrderRepository(),
        SqlOrderRepository(),
    ],
)
def test_lsp(repository):

    service = OrderService(repository)

    service.create_order(1, "Juan", 100.0)

    order = service.get_order(1)

    assert order is not None
    assert order.customer_name == "Juan"
