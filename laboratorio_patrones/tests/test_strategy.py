from laboratorio_patrones.patterns.strategy import BlackFridayPricing, VipPricing


def test_vip_pricing():
    strategy = VipPricing()

    assert strategy.apply_discount(100.0) == 80.0


def test_black_friday():
    strategy = BlackFridayPricing()

    assert strategy.apply_discount(100.0) == 50.0
