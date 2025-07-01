from fastapi.testclient import TestClient

from main import app
from schemas import Book
from db import fake_db
import pytest

# Fixture para limpiar la DB antes de cada test
@pytest.fixture(autouse=True)
def clean_db():
    fake_db.clear()
    yield

# Fixture para el cliente de prueba 
@pytest.fixture()
def client():
    # Retornar el cliente de prueba
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture(scope="module")
def json_headers():
    return {"Content-Type": "application/json"}

# Test 1: GET /books/ - Listar todos los libros (vacío y con datos)
def test_list_books_empty(client):
    response = client.get("/api/v1/books/")
    assert response.status_code == 200
    ob = response.json()
    assert len(ob) == 0
    # completar para asegurar que la estatus de respuesta sea 200 y la lista está vacía

# Test 2: POST /books/ - Crear un libro exitosamente
def test_add_book(client, json_headers):
    book_data = {"title": "Cien años de soledad", "author": "García Márquez", "year": 1967}
    response = client.post("/api/v1/books/", headers=json_headers, json=book_data)
    assert response.status_code == 200
    assert response.json()['message'] == 'Libro añadido' 
    assert response.json()['id'] == 0
    # verificar que responde  con 200, el mensaje obtenido es "Libro añadido"
    # y que el Id del json es 0

# Test 3: Devuelve una lista de libros en la DB
def test_list_books_with_data(client, json_headers):
    # Añadir un libro primero
    client.post("/api/v1/books/", headers=json_headers, json={"title": "El Principito", "author": "Saint-Exupéry", "year": 1943})
    # probar que el GET responde con status  200
    response = client.get("/api/v1/books/")
    ob = response.json()
    # probar que la longitud de la respuesta json es 1
    assert len(ob) == 1
    # probar que el título que devuelve es "El Principito"
    assert ob[0]['title'] == 'El Principito'


# Test 3: GET /books/{book_id} - Obtener un libro por ID
def test_get_book_exists(client, json_headers):
    # Añadir un libro y obtener su ID
    book_data = {"title": "1984", "author": "Orwell", "year": 1949}
    post_response = client.post("/api/v1/books/", headers=json_headers, json=book_data)
    book_id = post_response.json()["id"]
    # Verificar que el libro existe
    response = client.get("/api/v1/books/"+str(book_id))
    ob = response.json()
    # probar que al pedir el id, la respuesta es 200
    assert response.status_code == 200
    # probar que el título es "1984"
    assert ob['title'] == '1984'

# Test 4: GET /books/{book_id} - Libro no existe (error 404)
def test_get_book_not_found(client):
    # solilcitar un id inexistentes, por ejemplo :999
    response = client.get("/api/v1/books/"+str(999))
    ob = response.json()
    # probar que la respuesta es 404
    assert response.status_code == 404
    # probar que el detalles es "Libro no encontrado"
    assert ob['detail'] == 'Libro no encontrado'

# Test 5: Validación de datos con Pydantic (año negativo)
def test_add_book_invalid_data(client):
    invalid_book_data = {"title": "Libro Inválido", "author": "Anónimo", "year": -100}
    # tratar de incluir este libro en la db
    post_response = client.post("/api/v1/books/", json=invalid_book_data)
    assert post_response.status_code == 422
    # probar que FastAPI automáticamente retorna 422 si la validación falla