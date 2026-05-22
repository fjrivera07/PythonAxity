from laboratorio_solid.application.services import OrderService
from laboratorio_solid.infrastructure.memory_repository import MemoryOrderRepository
from laboratorio_solid.infrastructure.sql_repository import SqlOrderRepository


def main():

    print("=== Memory Repository ===")

    memory_repo = MemoryOrderRepository()
    service = OrderService(memory_repo)

    service.create_order(1, "Juan", 100.0)
    service.create_order(2, "Maria", 200.0)

    print(service.list_orders())

    print("\n=== SQL Repository ===")

    sql_repo = SqlOrderRepository()
    service = OrderService(sql_repo)

    service.create_order(3, "Pedro", 300.0)

    print(service.list_orders())


if __name__ == "__main__":
    main()
