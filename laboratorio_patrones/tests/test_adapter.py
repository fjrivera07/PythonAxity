from laboratorio_patrones.patterns.adapter import (
    ExternalPricingAdapter,
    ExternalPricingSystem,
)


def test_adapter():

    external = ExternalPricingSystem()
    adapter = ExternalPricingAdapter(external)

    price = adapter.get_price("A001")

    assert price == 100.0
