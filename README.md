# Curso de Python - Laboratorios y Proyecto Final

Repositorio de prácticas y proyectos desarrollados durante el módulo de formación, cubriendo conceptos de Python backend, Data Science y Arquitectura de Software.

---

# Contenido del repositorio

Este repositorio incluye:

- Laboratorios prácticos
- Ejercicios de arquitectura
- Proyecto final integrador

---

# Indice

- [Fundamental-Entorno y herramientas](./src/fjrb/laboratorio1-1.py)
- [Fundamental-Fundamentos del lenguaje](./src/fjrb/laboratorio2-1.py)
- [Fundamental-Funciones y programación “pythonic”-1](./src/fjrb/laboratorio3-1.py)
- [Fundamental-Funciones y programación “pythonic”-2](./src/fjrb/laboratorio3-2.py)
- [Fundamental-Objetos y modelos de datos](./laboratorio5_2/src/laboratorio5_2/main.py)
- [Fundamental-Tipado estático opcional y calidad](./laboratorio6_1/src/laboratorio6_1/main.py)
- [Fundamental-Librería estándar y E/S](./laboratorio7_1/src/laboratorio7_1/main.py)
- [Fundamental-HTTP y consumo de APIs (Smocker)](./laboratorio8_1/src/laboratorio8_1/main.py)

- [Intermediate-Acceso a datos y ORM](./laboratorio8_2/src/laboratorio8_2/main.py)
- [Intermediate-APIs web con FastAPI (Automatización)](./laboratorio_FastAPI/src/laboratorio_fastapi/main.py)
- [Intermediate-Pruebas y TDD](./laboratorio_FastAPI/tests/test_orders.py)
- [Intermediate-Concurrencia y rendimiento](./laboratorio_concurrencia/tests/test_async.py)
- [Intermediate-Principios SOLID aplicados en Python](./laboratorio_solid/src/laboratorio_solid/main.py)
- [Intermediate-Patrones de diseño](./laboratorio_patrones/src/laboratorio_patrones/main.py)
- [Intermediate-Ciencia de datos](./laboratorio_datascience/main.py)
- [Intermediate-Arquitectura Hexagonal (Puertos y Adaptadores)](./laboratorio_hexagonal/src/laboratorio_hexagonal/infrastructure/api/main.py)
- [Proyecto Final-Proyecto final integrador (Arquitectura Hexagonal/Limpia)](./orders_service/src/orders_service/api/main.py)


# Observaciones y notas 

- Procedimiento para crear y ambientar una solucion

        poetry new [nombreproyecto]
        poetry env info
            poetry env use 3.12
        poetry add --group dev mypy black isort ruff pre-commit pytest
        poetry install
        poetry run python -m [nombreproyecto]

- Paquetes

        poetry add httpx
        poetry add requests
        poetry add sqlalchemy alembic
        poetry add pandas polars numpy scikit-learn joblib
        poetry add --group dev pytest jupyter notebook

- Referencias:
        https://httpbin.org/delay
