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
$ pip freeze > requirements.txt
```

## Temario:

### - Pytest

Pytest es una libreria para poder testear los componentes de la aplicacion.

<!-- TODO: Hacer descripcion de como correr los test  -->