# import csv
# import json
# import logging
# import subprocess
# from datetime import UTC
# from datetime import datetime

# with open("usuarios.csv", newline="", encoding="utf-8") as archivo:
#     reader = csv.DictReader(archivo)
#     for fila in reader:
#         print(fila)

# datos = {
#     "nombre": "Greta",
#     "edad": 28
# }

# json_texto = json.dumps(datos, indent=2)
# print(json_texto)

# with open("datos.json", "w", encoding="utf-8") as archivo:
#     json.dump(datos, archivo, indent=2)

# with open("datos.json", "r", encoding="utf-8") as archivo:
#     datos_cargados = json.load(archivo)
#     print(datos_cargados)

# fecha_actual = datetime.now()
# print(fecha_actual)
# fecha_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
# print(fecha_formateada)

# ahora = datetime.now(UTC)
# print(ahora)

# logging.basicConfig(level=logging.INFO)
# logging.info("Aplicación iniciada")
# logging.warning("Esto es una advertencia")
# logging.error("Ocurrió un error")

# resultado = subprocess.run(
#     ["python", "--version"],
#     capture_output=True,
#     text=True,
# )

# print(resultado.stdout)
