import csv
from pathlib import Path


def leer_usuarios(ruta: Path):

    with ruta.open(
        mode="r",
        encoding="utf-8",
        newline="",
    ) as archivo:

        return list(csv.DictReader(archivo))
