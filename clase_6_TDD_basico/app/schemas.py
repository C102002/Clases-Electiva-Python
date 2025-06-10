from enum import Enum

from pydantic import BaseModel, Field

class Status(str, Enum):
    Success = "Success"
    Failed = "Failed"


class OperationBaseSchema(BaseModel):
    oper1: int | float = Field(..., description="primer operando")
    oper2: int | float = Field(..., description="segundo operando")


class OperationResult(OperationBaseSchema):
    result: int | float = None

class OperationResponse(BaseModel):
    status: Status
    operation_response:OperationResult