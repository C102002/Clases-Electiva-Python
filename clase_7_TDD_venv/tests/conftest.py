import uuid
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from fastapi.testclient import TestClient

from app.main import app
from app.database import Base, get_db

# SQLite database URL for testing
SQLITE_DATABASE_URL = "sqlite:///./test_db.db"

# Create a SQLAlchemy engine
engine = create_engine(
    SQLITE_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# Create a sessionmaker to manage sessions
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables in the database
Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """Crea una session de base de datos nueva para cada prueba individual con un rollback al final de la prueba."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def test_client(db_session):
    """Crea un cliente de prueba que establece como función de reemplazp override_get_db para la session de pruebas."""

    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client

# Fixture para generar un id aleatorio
@pytest.fixture()
def user_id() -> uuid.UUID:
    """Genera un id aleatorio para el usuario."""
    return str(uuid.uuid4())


# Fixture para generar el payload de usuario
@pytest.fixture()
def user_payload(user_id):
    """Genera un payload de usuario."""
    return {
        "id": user_id,
        "first_name": "John",
        "last_name": "Doe",
        "address": "123 Farmville",
    }


@pytest.fixture()
def user_payload_updated(user_id):
    """Genera un payload de actualización de usuario."""
    return {
        "first_name": "Jane",
        "last_name": "Doe",
        "address": "321 Farmville",
        "activated": True,
    }
