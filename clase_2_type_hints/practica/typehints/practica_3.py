
from typing import List, Optional

### Practica de ejemplo 3

y: List[int | float] = [2,3,4.1,5,6.2]
print(y)

# usado como retorno de una función
# def bs_to_usd(value:float) -> float | None:
#     try:
#         conversion_factor = 39
#         value = value/conversion_factor
#         return value
#     except TypeError:
#         return None
# usado como retorno de una función Optional

def bs_to_usd(value:float) -> Optional[float]:
    try:
        conversion_factor = 39
        value = value/conversion_factor
        return value
    except TypeError:
        return None
    


print(f"bs to dolar de 23: {'Error en la conversion' if bs_to_usd('23') is None else bs_to_usd('23')}")
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


class Job:
    def __init__(self,title:str,description:Optional[str]) -> None:
        self.title = title
        self.description = description

    def __repr__(self):
        return self.title


job1 = Job(title="SDE2",description="Sdfdk")
job2 = Job(title="Senior Manager", description="jfjdj")
# OJO Auqnue ponga el none ahi el optional tienes que mandarle el None
job3 = Job(title="pepe", description=None)

jobs: List[Job] = [job1,job2,job3]

print(f"todos los jobs son: {jobs}") 