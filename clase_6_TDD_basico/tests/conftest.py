import pytest
from fastapi.testclient import TestClient

from app.calculator.core import Calculator
from app.main import app
from app.schemas import OperationBaseSchema

@pytest.fixture(scope="function")
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="module")
def calculator():
    return Calculator(4, 8)

@pytest.fixture
def custom_calculator(scope="module"):
    def _calculator(a, b):
        return Calculator(a, b)

    return _calculator

@pytest.fixture(scope="module")
def json_headers():
    return {"Content-Type": "application/json"}

@pytest.fixture(scope="module")
def json_data():
    return {"oper1":6, "oper2":12}


