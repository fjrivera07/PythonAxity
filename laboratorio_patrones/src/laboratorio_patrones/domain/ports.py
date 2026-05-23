from typing import Protocol


class PriceProvider(Protocol):
    def get_price(self, product_code: str) -> float: ...
