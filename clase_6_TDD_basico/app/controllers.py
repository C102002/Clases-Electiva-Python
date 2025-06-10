from fastapi import APIRouter, HTTPException, status
from loguru import logger

from app import schemas
from app.calculator.core import Calculator

router = APIRouter()


@router.post("/add", status_code=status.HTTP_200_OK, response_model=schemas.OperationResponse)
def add_endpoint(payload: schemas.OperationBaseSchema):
    operands = payload.model_dump()

    oper1 = operands.get("oper1")
    oper2 = operands.get("oper2")

    result = Calculator(a=oper1, b=oper2).suma()

    operation_result = schemas.OperationResult(oper1=oper1, oper2=oper2, result=result)
    return schemas.OperationResponse(status=schemas.Status.Success, operation_response=operation_result)


@router.post("/subtract", status_code=status.HTTP_200_OK, response_model=schemas.OperationResponse)
def add_endpoint(payload: schemas.OperationBaseSchema):
    operands = payload.model_dump()

    oper1 = operands.get("oper1")
    oper2 = operands.get("oper2")

    result = Calculator(a=oper1, b=oper2).resta()

    operation_result = schemas.OperationResult(oper1=oper1, oper2=oper2, result=result)
    return schemas.OperationResponse(status=schemas.Status.Success, operation_response=operation_result)


@router.post("/multiply", status_code=status.HTTP_200_OK, response_model=schemas.OperationResponse)
def add_endpoint(payload: schemas.OperationBaseSchema):
    operands = payload.model_dump()

    oper1 = operands.get("oper1")
    oper2 = operands.get("oper2")

    result = Calculator(a=oper1, b=oper2).multiplica()

    operation_result = schemas.OperationResult(oper1=oper1, oper2=oper2, result=result)
    return schemas.OperationResponse(status=schemas.Status.Success, operation_response=operation_result)


@router.post("/divide", status_code=status.HTTP_200_OK, response_model=schemas.OperationResponse)
def add_endpoint(payload: schemas.OperationBaseSchema):
    operands = payload.model_dump()

    oper1 = operands.get("oper1")
    oper2 = operands.get("oper2")

    if oper2 == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No puede dividir entre cero"
        )


    result = Calculator(a=oper1, b=oper2).divide()

    operation_result = schemas.OperationResult(oper1=oper1, oper2=oper2, result=result)
    return schemas.OperationResponse(status=schemas.Status.Success, operation_response=operation_result)