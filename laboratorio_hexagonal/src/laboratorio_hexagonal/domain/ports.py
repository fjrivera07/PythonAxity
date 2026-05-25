from typing import Protocol

from .entities import Order


class OrderRepository(Protocol):
    def save(self, order: Order) -> None: ...


class NotificationPort(Protocol):
    def send(self, order: Order) -> None: ...
