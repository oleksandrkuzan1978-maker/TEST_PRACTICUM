import pytest


@pytest.fixture(scope="function")
def func_fixture():
    print("\n>>> CREATE function fixture")
    yield
    print("\n<<< DELETE function fixture")

@pytest.fixture(scope="session")
def session_fixture():
    print("\n>>> CREATE session fixture")
    yield
    print("\n<<< DELETE session fixture")

@pytest.fixture(scope="class")
def class_fixture():
    print("\n>>> CREATE class fixture")
    yield
    print("\n<<< DELETE class fixture")


@pytest.fixture(scope="module")
def module_fixture():
    print("\n>>> CREATE module fixture")
    yield
    print("\n<<< DELETE module fixture")





class TestUser:

    def test_one(
        self,
        func_fixture,
        class_fixture,
        module_fixture,
        session_fixture
    ):
        print("TEST ONE")

    def test_two(
        self,
        func_fixture,
        class_fixture,
        module_fixture,
        session_fixture
    ):
        print("TEST TWO")

    def test_three(
        self,
        func_fixture,
        class_fixture,
        module_fixture,
        session_fixture
    ):
        print("TEST THREE")