"""Тест загрузки файла test_file.txt и проверки его имени на странице результата."""

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_file_upload():
    """Загружает test_file.txt из папки модуля и проверяет имя загруженного файла."""
    # Запускаем Chrome и создаём сессию для управления браузером.
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/upload")
    # Получаем путь к файлу test_file.txt,
    # который находится в той же папке, что и этот Python-файл.
    #
    # __file__ — путь к текущему Python-файлу.
    # os.path.abspath(__file__) — получаем абсолютный путь.
    # os.path.dirname(...) — получаем папку с Python-файлом.
    # os.path.join(...) — добавляем к этой папке имя файла.
    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "test_file.txt"
    )
    # Находим HTML-поле выбора файла.
    file_input = driver.find_element(By.ID, "file-upload")
    # Передаём полю абсолютный путь к файлу без открытия системного диалога.
    file_input.send_keys(file_path)

    upload_button = driver.find_element(By.ID, "file-submit")
    # Делаем фиксированную паузу на 2 секунды; готовность элементов не проверяется.
    time.sleep(2)
    # Отправляем выбранный файл на сервер.
    upload_button.click()

    uploaded_file = driver.find_element(By.ID, "uploaded-files")
    # Делаем фиксированную паузу на 2 секунды; готовность элементов не проверяется.
    time.sleep(2)
    # Проверяем, что страница результата показывает ожидаемое имя файла.
    assert uploaded_file.text == 'test_file.txt'
