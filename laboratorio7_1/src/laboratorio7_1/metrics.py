def calcular_metricas(usuarios):

    total = len(usuarios)

    promedio = sum(int(u["edad"]) for u in usuarios) / total

    return {
        "total_usuarios": total,
        "edad_promedio": promedio,
    }
