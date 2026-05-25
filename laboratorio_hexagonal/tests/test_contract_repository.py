from laboratorio_hexagonal.domain.entities import Order
from laboratorio_hexagonal.infrastructure.repositories.memory import (
    InMemoryOrderRepository,
)


def test_repository_contract():
    repo = InMemoryOrderRepository()

    order = Order.create("Juan", 200)
    repo.save(order)

    assert len(repo.list_all()) == 1
    assert repo.list_all()[0].customer == "Juan"
