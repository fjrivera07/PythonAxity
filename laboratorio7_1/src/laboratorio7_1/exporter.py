import json
from pathlib import Path


def exportar_json(datos, ruta: Path):

    with ruta.open(
        mode="w",
        encoding="utf-8",
    ) as archivo:

        json.dump(
            datos,
            archivo,
            indent=2,
        )


# datos = [
#     {"nombre": "Francisco", "edad": 56},
#     {"nombre": "Magda", "edad": 57}
# ]
# path = Path("output/usuarios.json")
# print(path)
# exportar_json(datos, path)
