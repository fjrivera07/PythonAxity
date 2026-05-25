from ..domain.entities import Order
from ..domain.ports import NotificationPort, OrderRepository
from .dto import CreateOrderRequest, CreateOrderResponse


class CreateOrderUseCase:
    def __init__(self, repository: OrderRepository, notifier: NotificationPort):
        self.repository = repository
        self.notifier = notifier

    def execute(self, request: CreateOrderRequest) -> CreateOrderResponse:
        # 1. Crear entidad (reglas de dominio)
        order = Order.create(customer=request.customer, amount=request.amount)

        # 2. Guardar en repositorio (puerto)
        self.repository.save(order)

        # 3. Notificar (puerto)
        self.notifier.send(order)

        # 4. Responder DTO
        return CreateOrderResponse(
            id=order.id, customer=order.customer, amount=order.amount, status="created"
        )
