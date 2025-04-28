# somo se definió en 3.10:
from typing import List, TypeAlias

Matrix: TypeAlias = List[List[int | float]] # Una lista de listas de tipo flotante

a: Matrix = [[1, 2, 3], [4, 5, 6]]


# A aprtir de 3.12 se puede usar así:
from typing import List

type Matrix = List[List[int | float]]

b: Matrix = [[1, 2, 3], [4, 5, 6]]