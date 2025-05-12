# Considere el schema Pydantic siguiente:
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    price: float
    quantity: int = 1

# ¿Cuál es el valor predeetterminado del campo quantity ?

# Deberá ser 1, ya que es el valor por defecto que se le asigna en la definición del modelo.

item1=Item(name="item1", price=10.0)
item2=Item(name="item2", price=15.0)

print(f"Item 1: {item1}")
print(100*"-")
print(f"Item 2: {item2}")