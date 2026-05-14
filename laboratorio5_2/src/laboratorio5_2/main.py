from laboratorio5_2.mappers.order_mapper import to_entity, to_output
from laboratorio5_2.models.order_models import OrderIn


def main():

    entrada = OrderIn(
        quantity=2,
        unit_price=50,
    )

    order = to_entity(entrada)

    salida = to_output(order)

    print(salida.model_dump())


if __name__ == "__main__":
    main()
