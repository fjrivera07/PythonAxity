import requests

from ...domain.entities import Order
from ...domain.ports import NotificationPort


class HttpNotifier(NotificationPort):
    def __init__(self, endpoint: str = "https://example.com/notify"):
        self.endpoint = endpoint

    def send(self, order: Order) -> None:
        payload = {
            "order_id": order.id,
            "customer": order.customer,
            "amount": order.amount,
        }

        try:
            # Simulación de envío HTTP
            requests.post(self.endpoint, json=payload, timeout=2)
        except Exception as e:
            # En laboratorio no fallamos el flujo si notificación falla
            print(f"[NOTIFIER ERROR] {e}")
