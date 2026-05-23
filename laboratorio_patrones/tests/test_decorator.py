from laboratorio_patrones.application.pricing_service import PricingService
from laboratorio_patrones.domain.entities import Order
from laboratorio_patrones.patterns.adapter import (
    ExternalPricingAdapter,
    ExternalPricingSystem,
)
from laboratorio_patrones.patterns.strategy import VipPricing


def test_cached_price():

    provider = ExternalPricingAdapter(ExternalPricingSystem())

    service = PricingService(provider, VipPricing())

    order = Order(id=1, customer_type="vip", product_code="A001")

    first = service.calculate_price(order)
    second = service.calculate_price(order)

    assert first == second
