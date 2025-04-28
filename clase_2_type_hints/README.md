# Clase 2

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

### - Type Hints

Ya que Python no trae los tipos de datos y trabajaban todo con **Object**

```python
# Sin usar Type hits 
def greet(name):
    return f"Hola, {name}"

# Usando Type hits 
def greet(name: str) -> str:
return f"Hola, {name}"
```

### ¿Como lo pruebo?

Una vez instalada todas las dependencias

```bash
# Ejecutando esta porsion de codigo
mypy ejemplo_2_errado.py
```
Dando la siguiende salida
```bash
# ....
ejemplo_2_errado.py:4: error: Argument 1 to "total_price" has incompatible type "str"; expected "int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
# ....
```
>[!NOTE] 
>Cuando trabajes en el proyecto de FastAPI, deberías configurar un flujo que valide **TODO** 
>el type hint del proyecto automáticamente al ejecutarse o al realizar un commit. Esto es similar a lo que se hace en proyectos comunitarios.
>
> Para validar todos los archivos del proyecto, puedes usar el siguiente comando:
>
> ```bash
>#Ejemplo
> mypy .
> ```


#### Unión de tipos:
Especifica posibles múltiples tipos de una variable, parámetro o respuesta
```python
from typing import Union

def process_data(data: Union[int, float]) -> str o
def process_data(data: int | float) -> str: (desde Python 3.10+)

```
#### Tipos opcionales:

Se usa Optional para valores que pueden ser anulables

```python
from typing import Optional

def get_name() -> Optional[str]: o
def get_name -> str | None: #(desde Python 3.10+)

```
### - Métodos dunder

### - Funciones Generadoras

Es cuando no no deseamos sobreescribir los métodos iter() y next() para trabajar con una iteración todo el tiempo. Para ello usamos ***las funciones generadoras***. 


>[!NOTE] 
> ***Funcion generadora:*** Un generador o función generadora es una función que no devuelve un único valor, sino un objeto iterador (un iterable) con una secuencia de valores cuando se itera sobre él
>
>En Python, de forma similar a la definición de una función normal, podemos definir una función generadora utilizando la palabra clave **def**, pero en lugar de la sentencia return utilizamos la sentencia **yield**.
>```python
># Ejemplo
>def nombre_generador(arg):
># sentencias
>yield algo
>```