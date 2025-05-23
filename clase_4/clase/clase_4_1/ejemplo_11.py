# Validación de datos

from pydantic import BaseModel, field_validator, Field

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=3)
    email: str = Field(..., pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    age: int = Field(..., gt=18)
    
    # Validación de datos
    @field_validator('name')
    def name_must_contain_uppercase(cls, v):
        if not any(x.isupper() for x in v):
            raise ValueError('name must have at least one uppercase letter')
        return v
    
try:
    # Da error porque el nombre no tiene mayusculas
    user = User(id=1, name="pedro", email="pedro@test.com", age=23)
    print(user)
except ValueError as e:
    print(f"Error: {e}")