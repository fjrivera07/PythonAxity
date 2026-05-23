from laboratorio_patrones.domain.ports import PriceProvider


class ExternalPricingSystem:

    def calculate_amount(self, sku: str) -> float:
        prices = {
            "A001": 100.0,
            "B001": 200.0,
        }

        return prices.get(sku, 0.0)


class ExternalPricingAdapter(PriceProvider):

    def __init__(self, external_system: ExternalPricingSystem):
        self.external_system = external_system

    def get_price(self, product_code: str) -> float:
        return self.external_system.calculate_amount(product_code)
