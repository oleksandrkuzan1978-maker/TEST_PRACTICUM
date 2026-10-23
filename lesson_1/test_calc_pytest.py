from calculator import Calculator
import pytest

# @pytest.fixture
# def create_calculator():
#     return Calculator()

def test_sum_positive_numbers(create_calculator: Calculator):

    assert create_calculator.sum(2, 4) == 6
    assert create_calculator.sum(2, 5) == 7
    assert create_calculator.sum(1, 8) == 9


def test_sum_negative_numbers(create_calculator: Calculator):

    assert create_calculator.sum(-2, -4) == -6
    assert create_calculator.sum(-2, -5) == -7
    assert create_calculator.sum(-1, -8) == -9

@pytest.mark.skipif(condition="sys.version_info > (3, 8)", reason="Requires Python 3.8 or greater")   #@pytest.mark.skip(reason="Тестовый пропуск")
def test_division(create_calculator):
    assert  create_calculator.div(4, 2) == 2
    assert  create_calculator.div(8, 2) == 4
    assert  create_calculator.div(10, 5) == 2

#@pytest.mark.xfail(strict=True, reason="Метод в процессе разработки")
def test_division_by_zero(create_calculator):  #ZeroDivisionError("Division by zero")
    with pytest.raises(ZeroDivisionError, match="Division by zero"):
        create_calculator.div(4, 0)


#pytest --markers
