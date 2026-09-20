from simple_math import SimpleMath
import pytest

@pytest.fixture
def math_operation():
    return SimpleMath()


def test_square(math_operation):

    assert math_operation.square(3) == 9
    assert math_operation.square(-3) == 9
    assert math_operation.square(0) == 0


def test_cube(math_operation):

    assert math_operation.cube(3) == 27
    assert math_operation.cube(-3) == -27
    assert math_operation.cube(0) == 0

