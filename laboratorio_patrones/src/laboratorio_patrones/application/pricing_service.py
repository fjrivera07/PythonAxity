from laboratorio_patrones.domain.entities import Order
from laboratorio_patrones.domain.ports import PriceProvider
from laboratorio_patrones.patterns.decorator import cache_result
from laboratorio_patrones.patterns.strategy import PricingStrategy


class PricingService:

    def __init__(self, provider: PriceProvider, strategy: PricingStrategy):
        self.provider = provider
        self.strategy = strategy

    @cache_result
    def calculate_price(self, order: Order) -> float:

        base_price = self.provider.get_price(order.product_code)

        final_price = self.strategy.apply_discount(base_price)

        return final_price
