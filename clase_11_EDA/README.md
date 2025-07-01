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
pip freeze > requirements.txt
```

## Temario:

### - EDA (Event Driven Architecture)

## Correr el proyecto

### 1. Ejecutar el proyecto

En el root del proyecto *actor model*
```bash
# corre fastapi
uvicorn main:app --reload
```

En el root del proyecto *CQRS*

```bash
# corre fastapi
uvicorn main:app --reload
```

En el root del proyecto *event_sourcing*

```bash
# corre fastapi
uvicorn main:app --reload
```
En el root del proyecto *message_queue*

```bash
# corre fastapi
uvicorn main:app --reload
```

En el root del proyecto *pubsub*

```bash
# corre fastapi
uvicorn main:app --reload
```

En el root del proyecto *state_machine*

```bash
# corre fastapi
uvicorn main:app --reload
```