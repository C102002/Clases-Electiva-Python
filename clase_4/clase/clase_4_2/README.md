# Clase 4-2

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

### Extra añadir FastAPI

```bash
# Instala fast api
pip install fastapi

# Instala uvicorn que es donde se corre fastapi
pip install “uvicorn[standard]”
```

## Correr el proyecto

### 1. Ejecutar el proyecto

En el root del proyecto
```bash
# corre fastapi
uvicorn main:app –-reload
```

Si se corrio exitosamente deberia de salir algo similar a lo siguiente:
```bash
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [31528] using WatchFiles
INFO:     Started server process [20492]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

las ubicaciones de la documentacion si esta por defecto son las siguientes:

* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)


## Temario:

### - FastApi

FastAPI es un framework web moderno y de alto rendimiento diseñado específicamente para la creación de APIs, Fue creado por Sebastián Ramírez y liberado en 2018.
