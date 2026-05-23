from typing import Protocol


class PricingStrategy(Protocol):

    def apply_discount(self, price: float) -> float: ...


class RegularPricing:

    def apply_discount(self, price: float) -> float:
        return price


class VipPricing:

    def apply_discount(self, price: float) -> float:
        return price * 0.8


class BlackFridayPricing:

    def apply_discount(self, price: float) -> float:
        return price * 0.5
