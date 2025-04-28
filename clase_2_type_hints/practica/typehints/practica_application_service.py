from typing import Protocol, TypeVar, TypedDict, Generic, Optional

# Definir tipos genéricos
#! OJO: sino se pone eso de contravariante como en program 3 y haciendolo MANUAL no funciona
T = TypeVar('T', contravariant=True)  # Contravariante para el tipo de entrada
E = TypeVar('E', contravariant=True)  # Covariante para el tipo de salida

# Clase Result
class Result(Generic[T]):
    def __init__(self, value: Optional[T], error: Optional[Exception]) -> None:
        self.value = value
        self.error = error

    def __repr__(self) -> str:
        return f"Result(value={self.value}, error={self.error})"
    
    @staticmethod
    def success(value: T) -> "Result[T]":
        return Result(value=value, error=None)
    
    @staticmethod
    def fail(error: Exception) -> "Result[T]":
        return Result(value=None, error=error)
    
    def isSucsess(self) -> bool:
        return self.error is None

# Definir la interfaz genérica IApplicationService
class IApplicationService(Protocol[T, E]):
    def execute(self, data: T) -> Result[E]:
        pass

# DTOs para CreateProduct
class CreateProductAplicationEntryDTO(TypedDict):
    name: str
    price: int

# Implementación de CreateProduct
class CreateProduct:
    def execute(self, data: CreateProductAplicationEntryDTO) -> Result[None]:
        return Result.success(None)

# DTOs para CreateUser
class CreateUserAplicationEntryDTO(TypedDict):
    name: str
    cedula: str
    
class CreateUserAplicationResponseDTO(TypedDict):
    name: str

# Implementación de CreateUser
class CreateUser:
    def execute(self, data: CreateUserAplicationEntryDTO) -> Result[CreateUserAplicationResponseDTO]:
        return Result.fail(Exception("fallo"))
    
    
# Ejemplo
s1:CreateProduct= CreateProduct()

r1:Result[None]=s1.execute({"name":"pepe","price":45})

print(f"respuesta 1:{r1}")

s2:CreateUser=CreateUser()

r2:Result[CreateUserAplicationResponseDTO]=s2.execute({"name":"pepe","cedula":"12356"})

print(f"respuesta 2:{r2}")

