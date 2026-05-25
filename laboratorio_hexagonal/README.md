# Architecture Hexagonal Lab

## Run

```bash
poetry install
poetry run python main.py
```

## Tests

```bash
poetry run pytest
```

## Topics

- Pandas
- Polars
- NumPy
- scikit-learn
- joblib
- inference

## Install
- poetry add --group dev mypy black isort ruff pre-commit pytest
- poetry add fastapi uvicorn sqlalchemy pydantic requests
- fastapi → API
- uvicorn → servidor
- sqlalchemy → adaptador SQL
- pydantic → DTOs / request-response
- requests → notifier HTTP simulado
- pytest → pruebas
- httpx → tests e2e para FastAPI