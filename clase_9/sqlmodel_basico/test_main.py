# file: app/test_main.py
import pytest
from sqlmodel import SQLModel, Session, create_engine
from main import TESTING, engine, User, insert_user, get_all_users, get_user_by_id, update_user, delete_user

# Activa el modo de pruebas
TESTING = True

# Configuración de la base de datos de pruebas
@pytest.fixture(scope="function")
def setup_database():
    SQLModel.metadata.create_all(engine)  # Crea las tablas
    yield  # Ejecuta las pruebas
    SQLModel.metadata.drop_all(engine)  # Limpia después de las pruebas

# Pruebas unitarias
def test_insert_user(setup_database):
    user = insert_user("Test User", "test@example.com")
    assert user.id is not None
    assert user.name == "Test User"
    assert user.email == "test@example.com"

def test_get_all_users(setup_database):
    insert_user("User 1", "user1@example.com")
    insert_user("User 2", "user2@example.com")
    users = get_all_users()
    assert len(users) == 2
    assert users[0].name == "User 1"
    assert users[1].name == "User 2"

def test_get_user_by_id(setup_database):
    user = insert_user("Test User", "test@example.com")
    fetched_user = get_user_by_id(user.id)
    assert fetched_user is not None
    assert fetched_user.name == "Test User"

def test_update_user(setup_database):
    user = insert_user("Old Name", "old@example.com")
    updated_user = update_user(user.id, name="New Name", email="new@example.com")
    assert updated_user is not None
    assert updated_user.name == "New Name"
    assert updated_user.email == "new@example.com"

def test_delete_user(setup_database):
    user = insert_user("To Be Deleted", "delete@example.com")
    success = delete_user(user.id)
    assert success
    assert get_user_by_id(user.id) is None
