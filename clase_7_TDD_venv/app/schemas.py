from enum import Enum
from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, Field



class UserBaseSchema(BaseModel):

    id: UUID | None = None
    first_name: str = Field(..., description="El nombre del usuario", example="John")
    last_name: str = Field(..., description="El apellido del usuario", example="Doe")
    address: str | None = None
    activated: bool = False
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        from_attributes = True # Configurar el modelo para trabajar con atributos
        populate_by_name = True
        arbitrary_types_allowed = True


class Status(str, Enum):
    Success = "Success"
    Failed = "Failed"


class UserResponse(BaseModel):
    Status: Status
    User: UserBaseSchema


class GetUserResponse(BaseModel):
    Status: Status
    User: UserBaseSchema


class ListUserResponse(BaseModel):
    status: Status
    results: int
    users: List[UserBaseSchema]


class DeleteUserResponse(BaseModel):
    Status: Status
    Message: str
