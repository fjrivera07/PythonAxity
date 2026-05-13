def lotes(datos, tamaño):
    for i in range(0, len(datos), tamaño):
        yield datos[i : i + tamaño]


numeros = list(range(1, 11))

for lote in lotes(numeros, 3):
    print(lote)
