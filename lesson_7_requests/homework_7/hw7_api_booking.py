import requests
from variables import *
class BookerApi:
    """Класс для взаимодействия с API Restful-Booker"""
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def get_auth_token(self, username='admin', password='password123'):
        """Получение токена авторизации"""
        payload = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/auth", json=payload)
        assert response.status_code == 200, f"Ошибка авторизации: {response.status_code}"
        return response.json()["token"]

    def get_booking_ids(self, params=None):
        """Получить список всех ID бронирований (с фильтрацией или без)"""
        response = requests.get(f"{self.base_url}/booking", params=params)
        assert response.status_code == 200, f"Ошибка получения списка: {response.status_code}"
        return response.json()

    def get_booking(self, booking_id):
        """Получить детали бронирования по ID"""
        response = requests.get(f"{self.base_url}/booking/{booking_id}")
        return response

    def create_booking(self, booking_data):
        """Создать новое бронирование"""
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        response = requests.post(f"{self.base_url}/booking", json=booking_data, headers=headers)
        return response.json()

    def update_booking(self, booking_id, booking_data, token):
        """Полное обновление бронирования (PUT)"""
        headers = {"Content-Type": "application/json",
                   "Accept": "application/json",
                   "Cookie": f"token={token}"}
        response = requests.put(f"{self.base_url}/booking/{booking_id}", json=booking_data, headers=headers)
        return response

    def partial_update_booking(self, booking_id, update_data, token):
        """Частичное обновление бронирования (PATCH)"""
        headers = {"Content-Type": "application/json",
                   "Accept": "application/json",
                   "Cookie": f"token={token}"}
        response = requests.patch(f"{self.base_url}/booking/{booking_id}", json=update_data, headers=headers)
        return response

    def delete_booking(self, booking_id, token):
        """Удаление бронирования (DELETE)"""
        headers = {"Content-Type": "application/json",
                   "Cookie": f"token={token}"}
        response = requests.delete(f"{self.base_url}/booking/{booking_id}", headers=headers)
        return response
