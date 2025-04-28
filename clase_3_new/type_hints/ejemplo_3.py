# For python version <=3.9
from typing import List, Tuple, Dict , Union


# Anotando estructuras de datos
price: List[int] = [213,234,984]
immutable_price: Tuple[int,int,int] = (231,983,704)
price_dict: Dict[str,int] = {
    'item_1' : 340,
    'item_2' : 500,
}

print(price)
print(immutable_price)
print(price_dict)

# Anotando structuras de datos complejas:
x: List[Union[int, float]] = [2,3,4.1,5,6.2]
print(x)

y: List[int | float] = [2,3,4.1,5,6.2]
print(y)

# usado como retorno de una función
def bs_to_usd(value:float) -> float | None:
    try:
        conversion_factor = 39
        value = value/conversion_factor
        return value
    except TypeError:
        return None

print(bs_to_usd('23'))

# usando nuestros propios tipos:
# ejemplo 1
Image = List[List[int]]

def flatten_image(image: Image)->List:  #custom type Image
    flat_list = []
    for sublist in image:
        for item in sublist:
            flat_list.append(item)
    return flat_list

image = [[1,2,3],[4,5,6]]
print(flatten_image(image))

from typing import Optional

class Job:
    def __init__(self,title:str,description:Optional[str]) -> None:
        self.title = title
        self.description = description

    def __repr__(self):
        return f"Job({self.title}, {self.description})"


job1 = Job(title="SDE2",description="Sdfdk")
job2 = Job(title="Senior Manager", description=None)

jobs: List[Job] = [job1,job2] 
print(jobs)