from laboratorio_patrones.application.pricing_service import PricingService
from laboratorio_patrones.domain.entities import Order
from laboratorio_patrones.patterns.adapter import (
    ExternalPricingAdapter,
    ExternalPricingSystem,
)
from laboratorio_patrones.patterns.strategy import BlackFridayPricing, VipPricing


def main():

    external = ExternalPricingSystem()
    provider = ExternalPricingAdapter(external)

    order = Order(id=1, customer_type="vip", product_code="A001")

    print("=== VIP Pricing ===")

    vip_service = PricingService(provider, VipPricing())

    print(vip_service.calculate_price(order))

    print(vip_service.calculate_price(order))

    print("\n=== Black Friday ===")

    bf_service = PricingService(provider, BlackFridayPricing())

    print(bf_service.calculate_price(order))


if __name__ == "__main__":
    main()
