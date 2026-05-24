import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from orders_service.api.dependencies import get_db
from orders_service.api.main import app
from orders_service.infrastructure.db.base import Base

# DB de pruebas
TEST_DATABASE_URL = "sqlite:///./test_orders.db"

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client():
    # Crear tablas en la DB de pruebas
    Base.metadata.create_all(bind=engine)

    # Override de dependencia FastAPI
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as client:
        yield client

    # Limpiar overrides
    app.dependency_overrides.clear()

    # Cerrar sesiones abiertas
    TestingSessionLocal.close_all()

    # Eliminar tablas
    Base.metadata.drop_all(bind=engine)

    # Liberar conexiones SQLite (importante en Windows)
    engine.dispose()

    # Borrar archivo físico
    if os.path.exists("test_orders.db"):
        os.remove("test_orders.db")
