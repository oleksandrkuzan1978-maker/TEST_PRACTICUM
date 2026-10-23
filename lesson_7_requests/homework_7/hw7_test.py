from operator import and_

import pytest

from hw7_api import BookerApi

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture
def api():
    return BookerApi(BASE_URL)


@pytest.fixture
def auth_token(api):
    """Фикстура для получения токена перед тестами, требующими прав"""
    return api.get_auth_token("admin", "password123")


@pytest.fixture
def sample_booking():
    """Тестовые данные для создания брони"""
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-10"
        },
        "additionalneeds": "Breakfast"
    }
# ------------------- ТЕСТЫ -------------------

def test_user_authorization(api):
    """Тест: получение токена авторизации"""
    token = api.get_auth_token("admin", "password123")
    assert token is not None and len(token) > 0, "Токен не должен быть пустым"
