# Clase 7

## ¿Como correrlo?

### 1. Crear el ambiente virtual de Python

```bash
# Ejecuta el siguiente comando para crear el ambiente virtual en la ruta de la clase
python -m venv venv
```

### 2. Activa el ambiente virtual

```bash
# Windows (usando el Command Prompt):
venv\Scripts\activate

# Windows (usando PowerShell):
.\venv\Scripts\activate.ps1

# macOs y Linux:
source venv/bin/activate
```
### 3. Descargar las dependencias
```bash
# Ejecutar el siguiente comando
pip install -r requirements.txt
```

### 4. Actualizar dependencias

```bash
# Ejecutar el siguiente comando
$ pip freeze > requirements.txt
```

## Temario:

# Proyecto de Ejemplo de DDD: Biblioteca Digital

Este proyecto de ejemplo utiliza el enfoque de Desarrollo Orientado al Dominio (DDD) para estructurar y organizar el código de una biblioteca digital. Primero vas a encontrar instrucciones para poner el proyecto en funcionamiento, a continuación se explica cómo se relacionan los conceptos de DDD con cada parte del código.

# Instrucciones para Arrancar y Ejecutar el Proyecto

Este documento proporciona una guía paso a paso para arrancar y ejecutar el proyecto de ejemplo de DDD de la Biblioteca Digital.

## Requisitos Previos

Asegúrate de tener instalados los siguientes programas en tu sistema:

1. **Docker** - Puedes descargarlo e instalarlo desde [aquí](https://www.docker.com/get-started).
2. **Docker Compose** - Normalmente viene incluido con la instalación de Docker.

## Construir y Ejecutar el Proyecto con Docker Compose
### Paso 1: Construir las Imágenes de Docker
Construye las imágenes de Docker especificadas en el archivo docker-compose.yml:
```bash
docker compose build
```
### Paso 2: Iniciar los Servicios
Inicia los servicios definidos en el archivo `docker-compose.yml`:
```bash
docker compose up
```
Este comando levantará los contenedores de la aplicación web y la base de datos SQLite. La aplicación web estará disponible en http://localhost:8000.

## Probar la Aplicación
Una vez que los contenedores estén en funcionamiento, puedes probar la aplicación utilizando un navegador web o herramientas como `curl` o `Postman`, o directamente con `Swagger`, que viene integrado en la aplicación, este último lo revisas en la dirección:
```bash
http://localhost:8000/docs
```
### Añadir un Nuevo Libro
Realiza una petición POST a la siguiente URL para añadir un nuevo libro:
```bash
http://localhost:8000/books/
```
Utiliza el siguiente cuerpo JSON en la solicitud:
```json
{
    "title": "El Nombre del Viento",
    "author": "Patrick Rothfuss",
    "isbn": "9788401352836"
}
```

### Obtener Todos los Libros
Puedes realizar una petición GET a la siguiente URL para obtener todos los libros:
```bash
http://localhost:8000/books/
```

### Detener los Servicios
Para detener los servicios, usa el siguiente comando:
```bash
docker compose down
```
Esto detendrá y eliminará los contenedores, redes y volúmenes creados por `docker-compose up`.


## Conceptos Claves de DDD

### Entidades

**Definición:** Una entidad es un objeto con una identidad distinta que atraviesa diferentes estados durante su vida.

**Implementación:**
```python
# app/domain/schemas.py
class Book(BaseModel):
    id: int
    title: str
    author: str
    isbn: str = Field(min_length=10, max_length=13)

    model_config = ConfigDict(
        from_attributes=True
    )
```
### Objetos de Valor

**Definición:** Un objeto de valor es un objeto que se define solo por sus atributos y no tiene identidad propia.

**Implementación:**
```python
# app/domain/schemas.py
class ISBN(BaseModel):
    value: str = Field(min_length=10, max_length=13)
```
### Agregados

**Definición:** Un agregado es un conjunto de entidades y objetos de valor que se tratan como una única unidad.

**Implementación:**
```python
# app/domain/aggregates.py
class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: BookCreate) -> Book:
        new_book = Book(id=len(self.books) + 1, title=book.title, author=book.author, isbn=book.isbn)
        self.books.append(new_book)
        return new_book

    def get_all_books(self) -> List[Book]:
        return self.books
```
### Repositorios

**Definición:** Un repositorio es una colección de objetos de dominio que imita una colección en memoria de objetos, permitiendo agregar, eliminar y recuperar objetos.

**Implementación:**
```python
# app/domain/repositories.py
class BookRepository(ABC):

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass

    @abstractmethod
    def add_book(self, book: BookCreate) -> Book:
        pass
```
### Servicios de Dominio

**Definición:** Un servicio de dominio contiene lógica que no pertenece a una entidad u objeto de valor en particular.

**Implementación:**
```python
# app/domain/services.py
class LibraryService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def get_all_books(self) -> list[Book]:
        return self.repository.get_all_books()

    def add_book(self, book: BookCreate) -> Book:
        return self.repository.add_book(book)
```
### Eventos de Dominio

**Definición:** Un evento de dominio representa algo que ha sucedido en el dominio que los interesados quieren que sepan.

**Implementación:**
```python
# app/domain/domain_events.py
class BookAddedEvent(BaseModel):
    book_id: int
```

## Patrones de DDD
### Patrón Entidad
**Implementación:**
```python
# app/domain/schemas.py
class Book(BaseModel):
    id: int
    title: str
    author: str
    isbn: constr(min_length=10, max_length=13)

    class Config:
        orm_mode = True
```
### Patrón Objeto de Valor
**Implementación:**
```python
# app/domain/schemas.py
class ISBN(BaseModel):
    value: constr(min_length=10, max_length=13)
```
### Patrón Fábrica
**Implementación:**En este ejemplo, la función add_book de la clase Library actúa como una fábrica creando instancias de Book.
```python
# app/domain/aggregates.py
class Library:
    def add_book(self, book: BookCreate) -> Book:
        new_book = Book(id=len(self.books) + 1, title=book.title, author=book.author, isbn=book.isbn)
        self.books.append(new_book)
        return new_book
```
### Patrón Repositorio
**Implementación:**
```python
# app/infrastructure/repositories_impl.py
class SQLAlchemyBookRepository(BookRepository):
    def __init__(self):
        self.db: Session = SessionLocal()

    def get_all_books(self) -> list[Book]:
        books = self.db.query(BookModel).all()
        return [Book.from_orm(book) for book in books]

    def add_book(self, book: BookCreate) -> Book:
        db_book = BookModel(title=book.title, author=book.author, isbn=book.isbn)
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return Book.from_orm(db_book)
```

## Arquitectura de Capas
### Capa de Dominio
**Descripción:** Contiene la lógica de negocio central, entidades, agregados, objetos de valor, servicios de dominio y eventos de dominio.

**Implementación**:
```python
# app/domain/schemas.py
# app/domain/aggregates.py
# app/domain/repositories.py
# app/domain/services.py
# app/domain/domain_events.py
```
### Capa de Aplicación
**Descripción:** Maneja la lógica de la aplicación y la coordinación de las tareas, interactuando con la capa de dominio.

**Implementación**:
```python
# app/api/routes.py
from fastapi import APIRouter, Depends, HTTPException
from app.domain.services import LibraryService
from app.domain.schemas import BookCreate, Book
from app.infrastructure.repositories_impl import SQLAlchemyBookRepository

router = APIRouter()

def get_library_service():
    repository = SQLAlchemyBookRepository()
    return LibraryService(repository)

@router.get("/books/", response_model=list[Book])
def get_books(library_service: LibraryService = Depends(get_library_service)):
    return library_service.get_all_books()

@router.post("/books/", response_model=Book)
def add_book(book: BookCreate, library_service: LibraryService = Depends(get_library_service)):
    return library_service.add_book(book)
```
### Capa de Infraestructura
**Descripción:** Proporciona implementaciones de los repositorios, acceso a bases de datos y otros servicios externos necesarios.

**Implementación**:
```python
# app/infrastructure/orm.py
# app/infrastructure/repositories_impl.py
# app/infrastructure/database.py
```
