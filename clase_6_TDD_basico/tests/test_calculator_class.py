import pytest

def test_add(calculator):
    assert calculator.suma() == 12


def test_subtract(calculator):
    assert calculator.resta() == -4


def test_multiply(calculator):
    assert calculator.multiplica() == 32


def test_divide(calculator):
    assert calculator.divide() == 0.5


def test_divide_by_zero(calculator):
    calculator.b = 0
    with pytest.raises(ZeroDivisionError):
        calculator.divide()


# Advanced Calculator Testing with Dynamic Fixture
def test_add_advanced(custom_calculator):
    assert custom_calculator(10, 20).suma() == 30


def test_subtract_advanced(custom_calculator):
    assert custom_calculator(10, 20).resta() == -10


def test_multiply_advanced(custom_calculator):
    assert custom_calculator(10, 20).multiplica() == 200


def test_divide_advanced(custom_calculator):
    assert custom_calculator(10, 20).divide() == 0.5


def test_divide_by_zero_advanced(custom_calculator):
    with pytest.raises(ZeroDivisionError):
        custom_calculator(10, 0).divide()