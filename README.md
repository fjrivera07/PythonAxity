
    Procedimiento para crear y ambientar una solucion
        poetry new [nombreproyecto]
        poetry env info
            poetry env use 3.12
        poetry add --group dev mypy black isort ruff pre-commit pytest
        poetry install
        poetry run python -m [nombreproyecto]

        poetry add httpx
        poetry add requests
        poetry add sqlalchemy alembic

    Consideraciones:
        Para los laboratorios de los temas 1-4 se crearon carpetas
        Para los siguientes laboratorios se crearon proyectos
        En el proyecto laboratorio_fastapi se implemento el tema Intermediate-Pruebas-TDD en la carpeta de tests

    Referencias:
        https://httpbin.org/delay
    
    Observaciones:
    S - SRP (Single Responsibility Principle)
    O - OCP (Open/Closed Principle)
    L - LSP (Liskov Substitution Principle)
    I - ISP (Interface Segregation Principle)
    D - DIP (Dependency Inversion Principle)
    
    En la capa de Domain se define la entidad de negocio y los contratos (puertos o interfaces) que representan las dependencias que el dominio necesita, como el repositorio.
    En la capa de Application se implementan los casos de uso o servicios de aplicación, que orquestan la lógica del negocio y reciben por inyección de dependencias esos contratos definidos en el dominio.
    Finalmente, en la capa de Infrastructure se crean las implementaciones concretas de esos contratos, encargándose de la comunicación con tecnologías externas como bases de datos, APIs o sistemas de mensajería.
