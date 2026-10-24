import pytest

from hw7_api_booking import BookerApi
from variables import *

@pytest.fixture
def api():
    return BookerApi(BASE_URL)


@pytest.fixture
def auth_token(api):
    """Фикстура для получения токена перед тестами, требующими прав"""
    return api.get_auth_token(username, password)


@pytest.fixture
def sample_booking():
    """Тестовые данные для создания брони"""
    return booking_data

# ------------------- ТЕСТЫ -------------------

def test_user_authorization(api):
    """Тест: получение токена авторизации"""
    token = api.get_auth_token(username, password)
    assert token is not None and len(token) > 0, token_message

def test_create_booking(api, sample_booking):
    """Тест: создание бронирования и проверка сохраненных данных"""
    created_data = api.create_booking(sample_booking)
    assert "bookingid" in created_data
    assert created_data["booking"]["bookingdates"]["checkin"] == sample_booking["bookingdates"]["checkin"]
    assert created_data["booking"]["bookingdates"]["checkout"] == sample_booking["bookingdates"]["checkout"]


def test_patch_booking(api, auth_token, sample_booking):
    """Тест: частичное изменение бронирования (PATCH)"""
    created = api.create_booking(sample_booking)
    booking_id = created["bookingid"]

    patch_payload = payload

    response = api.partial_update_booking(booking_id, patch_payload, auth_token)
    assert response.status_code == 200

    patched_data = response.json()
    # Проверяем измененные поля
    assert patched_data["firstname"] == "Emmanuil"
    assert patched_data["additionalneeds"] == "Any other needs the guest has"
    # Проверяем, что нетронутые поля сохранили старое значение
    assert patched_data["lastname"] == sample_booking["lastname"]


def test_get_booking_by_id(api, sample_booking):
    """Тест: получение бронирования по ID"""
    created = api.create_booking(sample_booking)
    booking_id = created["bookingid"]
    print(created)
    response = api.get_booking(booking_id)
    assert response.status_code == 200

    data = response.json()
    assert data["firstname"] == "Maria"
    assert data["lastname"] == "Brucks"


def test_get_booking_by_nonexistent_id(api):
    """Тест: получение бронирования по несуществующему ID."""
    nonexistent_id = 999999999  # ID должен отсутствовать в тестовых данных

    response = api.get_booking(nonexistent_id)

    assert response.status_code == 404