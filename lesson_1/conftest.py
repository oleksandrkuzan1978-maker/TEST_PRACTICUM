import pytest
from calculator import Calculator

@pytest.fixture(scope="module") #@pytest.fixture(scope="function"), @pytest.fixture(scope="session") @pytest.fixture(scope="class")
def create_calculator():
    return Calculator()