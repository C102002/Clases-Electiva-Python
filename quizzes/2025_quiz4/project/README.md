# API de Gestión de Biblioteca (Evaluación Parcial)

Este proyecto implementa una API RESTful básica para la gestión de una biblioteca, utilizando **FastAPI** para la API, **SQLModel** para la interacción con la base de datos, **Alembic** para las migraciones del esquema de la base de datos y **Docker** para la contenerización.

Este repositorio es el punto de partida para su **Quiz No. 4**. Se les proporciona una estructura base funcional y su tarea será extenderla para añadir nuevas funcionalidades.

## ⚠️ Recuerde completar los datos en el archivo *integrantes.txt*

## 🚀 Configuración del Proyecto

Sigue estos pasos para levantar el entorno de desarrollo y la API:

1.  **Clonar el Repositorio:**
    ```bash
    git clone <URL_DE_TU_REPOSITORIO>
    cd <nombre_del_directorio_clonado>
    ```

2.  **Levantar el Entorno Docker:**
    Asegúrate de tener Docker y Docker Compose instalados. Luego, desde la raíz del proyecto, ejecuta:
    ```bash
    docker-compose up --build -d
    ```
    Esto construirá las imágenes, levantará los servicios (base de datos PostgreSQL, la aplicación FastAPI y pgAdmin) y aplicará la migración inicial de Alembic que crea la tabla `authors`.

    **⚠️ NOTA IMPORTANTE:** La aplicación FastAPI se ejecutará dentro de los contenedores. Deberán averiguar cómo acceder a ella desde su navegador.

3.  **Verificar el Estado de la API:**
    Una vez que los contenedores estén en ejecución (puede tomar un momento para que la base de datos esté lista), puedes verificar el estado de la API:

    * **Health Check:**
        Abrir en el navegador: `http://localhost:<PUERTO_DEL_CONTENEDOR>/healthcheck`
        Deberías ver: `{"message": "api working!"}`

    * **Documentación Interactiva (Swagger UI):**
        Abrir en el navegador: `http://localhost:<PUERTO_DEL_CONTENEDOR>/docs`
        Aquí podrás ver la documentación de los endpoints existentes para `Authors`.

    * **Acceso a pgAdmin:**
        Abrir en el navegador: `http://localhost:5050`
        Credenciales:
        * **Email:** `admin@admin.com`
        * **Contraseña:** `admin`
        Podrás conectarte a la base de datos `library` (host `db`, puerto `5432`, usuario `postgres`, contraseña `postgres`) y verificar la tabla `authors` ya creada.

## 🎯 Ejercicios de Evaluación (Quiz Nº 4)

Partiendo del código base provisto, su equipo debe extender la API para gestionar los **Libros** asociados a los autores existentes.

**Tiempo Límite:** 30 minutos

**Tareas a Realizar:**

1.  **Crear nuevos modelos SQLModel para `Book`:**
    * En `app/models.py`, creen un nuevo modelo llamado `Book` (y sus variantes `BookBase`, `BookCreate`, `BookRead`) con los siguientes campos:
        * `id`: Clave primaria autoincremental (tipo entero).
        * `title`: Título del libro (cadena de texto, obligatorio).
        * `year`: Año de publicación (entero, opcional).
        * `author_id`: Clave foránea que apunte al `id` de la tabla `authors`. Este campo debe ser **obligatorio** al crear un libro.

2.  **Generar y aplicar una nueva migración de Alembic:**
    * Dentro del contenedor `web` (pueden acceder con `docker-compose exec web bash`), utilicen Alembic para generar una **nueva migración** que cree la tabla `books` con el campo `author_id` y su restricción de clave foránea a la tabla `authors`.
    * **No utilicen `autogenerate` directamente en el archivo de migración final**. Generen el archivo con `alembic revision -m "Create books table and add author foreign key"` y luego editen el contenido del `upgrade()` y `downgrade()` para declarar la tabla `books` y su `ForeignKeyConstraint` manualmente.
    * Para declarar la clave foránea directamente en la creación de la tabla `books` en Alembic, usarán `sa.ForeignKeyConstraint()` como un argumento en `op.create_table()`. La sintaxis general es:
        ```python
        sa.ForeignKeyConstraint(
            ['nombre_columna_local'],      # Columna(s) en la tabla que se está creando
            ['nombre_tabla_remota.nombre_columna_remota'], # Columna(s) en la tabla referenciada
            name='nombre_de_la_restriccion',
            ondelete='CASCADE'             # Comportamiento al eliminar el padre
        )
        ```
    * Apliquen esta migración para actualizar el esquema de la base de datos: `alembic upgrade head`.

3.  **Implementar nuevos Endpoints en FastAPI para `Book`:**
    * Creen un nuevo archivo en `app/routers/` (ej. `books.py`) y definan un `APIRouter` para la gestión de libros.
    * Creen un endpoint **POST** en `/books` que permita añadir nuevos libros a la base de datos.
        * Debe aceptar un `BookCreate` como cuerpo de la solicitud (que incluirá el `author_id`).
        * Debe retornar el libro creado con su `id`.
        * **(BONUS - Si el tiempo lo permite):** Incluyan una validación para asegurar que el `author_id` proporcionado exista en la base de datos antes de crear el libro.
    * Creen un endpoint **GET** en `/books` que retorne una lista de todos los libros.
    * Creen un endpoint **GET** en `/authors/{author_id}/books` que retorne una lista de todos los libros asociados a un `author_id` específico.
    * Asegúrense de incluir su nuevo router de libros en `app/main.py` usando `app.include_router()`.

**Requisitos para la Entrega:**

* El equipo debe ser capaz de mostrar una demostración funcional de los nuevos endpoints de `Book` (`POST /books`, `GET /books`, `GET /authors/{author_id}/books`) utilizando la interfaz de Swagger UI (`/docs`).
* Deben mostrar el nuevo archivo de migración generado por Alembic para la tabla `books` (su contenido manual).
* Deben explicar brevemente los cambios realizados en los modelos y en los endpoints.

## 📚 Recursos Adicionales (¡Útiles para el Ejercicio!)

* **Documentación de SQLModel - Definición de Modelos con Claves Foráneas:**
    Revisen cómo se declara un campo `Field` que es una clave foránea en SQLModel (útil para la definición de su modelo `Book`):
    [Tutorial de SQLModel: Crear Tablas Conectadas](https://sqlmodel.tiangolo.com/tutorial/connect/create-connected-tables/)

* **Documentación de SQLAlchemy Core - `ForeignKeyConstraint`:**
    Este es el componente fundamental de SQLAlchemy que permite definir claves foráneas a nivel de tabla. Aunque es una documentación de bajo nivel, es la base de la sintaxis que usarán en Alembic para `op.create_table()`.
    [Documentación de SQLAlchemy: `sqlalchemy.schema.ForeignKeyConstraint`](https://docs.sqlalchemy.org/en/20/core/constraints.html#defining-foreign-keys)

---