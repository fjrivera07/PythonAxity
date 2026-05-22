
    Procedimiento para crear y ambientar una solucion
        poetry new [nombreproyecto]
        poetry env info
            poetry env use 3.12
        poetry add --group dev mypy black isort ruff pre-commit pytest
        poetry install
        poetry run python -m [nombreproyecto]

    En el proyecto laboratorio_fastapi se implemento el tema Intermediate-Pruebas-TDD en la carpeta de tests

    Referencias:
        
        https://httpbin.org/delay