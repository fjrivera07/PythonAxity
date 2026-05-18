import logging
from pathlib import Path

from laboratorio7_1.exporter import exportar_json
from laboratorio7_1.metrics import calcular_metricas
from laboratorio7_1.reader import leer_usuarios

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def main() -> None:
    logging.info("Inicio proceso")
    ruta_csv = Path("data/usuarios.csv")
    usuarios = leer_usuarios(ruta_csv)
    metricas = calcular_metricas(usuarios)
    salida = Path("output/metricas.json")
    exportar_json(metricas, salida)
    logging.info("Archivo JSON generado")


if __name__ == "__main__":
    main()
