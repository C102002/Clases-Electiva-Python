# Clase 6

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

### - OAuth2 y Jwt

## Correr el proyecto

### 1. Ejecutar el proyecto

En el root del proyecto basic
```bash
# corre fastapi
uvicorn main_1:app --reload
```

En el root del proyecto paso 2

```bash
# corre fastapi
uvicorn main_2:app --reload
```

En el root del proyecto paso 3

```bash
# corre fastapi
uvicorn main_3:app --reload
```
En el root del proyecto paso 4

```bash
# corre fastapi
uvicorn main_4:app --reload
```