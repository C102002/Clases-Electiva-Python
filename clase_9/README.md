# Clase 9

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

### - SQLModel, ASYnc y Alembic

#### SQLModel

SQLModel es una biblioteca que combina lo mejor de SQLAlchemy y Pydantic para facilitar la definición de modelos de datos, realizar validaciones y ejecutar operaciones CRUD en bases de datos relacionales. Utilizando SQLModel, puedes definir tus tablas de forma declarativa y aprovechar la verificación automática de tipos y validaciones de datos. Esta integración simplifica el desarrollo y mantenimiento de aplicaciones que requieren trabajar de forma directa y segura con la información almacenada en la base de datos. Además, SQLModel se integra de manera natural en aplicaciones asíncronas, brindando fluidez y eficiencia en el manejo de operaciones de entrada/salida.

#### Programación Asíncrona (Async)

La programación asíncrona en Python permite gestionar múltiples tareas concurrentemente sin bloquear la ejecución del programa. Utilizando el módulo asyncio y las palabras clave async y await, puedes optimizar el rendimiento de operaciones de entrada/salida, como conexiones a bases de datos, peticiones HTTP o cualquier otra tarea que implique espera. Esta aproximación es ideal para aplicaciones web o microservicios que requieren gestionar muchas conexiones simultáneas con alta eficiencia. Al implementar funciones asíncronas, el código se vuelve más escalable y responsivo, mejorando la experiencia del usuario al reducir la latencia en procesos críticos.

#### Alembic

Alembic es una herramienta de migraciones de bases de datos que se integra con SQLAlchemy. Con Alembic, puedes gestionar y versionar los cambios en el esquema de la base de datos de manera controlada y reproducible. Cada vez que realizas modificaciones en tus modelos (por ejemplo, agregar o eliminar columnas), Alembic te ayuda a generar un script de migración que se puede aplicar de forma incremental. Esta herramienta es esencial para mantener la integridad de la base de datos, facilitando la actualización y despliegue de las aplicaciones en diferentes entornos sin perder el historial o la estructura de los datos.
