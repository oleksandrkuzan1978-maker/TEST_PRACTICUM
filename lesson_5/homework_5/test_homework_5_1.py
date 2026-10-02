"""Тест наличия заданного фрагмента текста внутри iframe."""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

@pytest.fixture
def browser():
    """Создаёт Chrome и передаёт его тесту через yield.

    После завершения теста закрывает браузер и завершает сессию WebDriver."""
    # Запускаем Chrome и создаём сессию для управления браузером.
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Задаём ожидание при поиске элементов; это не фиксированная пауза.
    driver.implicitly_wait(10)
    # Передаём драйвер тесту; код ниже выполнится при завершении фикстуры.
    yield driver

    driver.quit()

def test_find_element_text(browser):
    """Проверяет, что текст body первого iframe содержит заданный фрагмент."""
    url = "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"
    browser.get(url)

    # Находим первый iframe на странице.
    iframe = browser.find_element(By.TAG_NAME, "iframe")

    # Переключаем поиск элементов внутрь найденного iframe.
    browser.switch_to.frame(iframe)
    # Получаем body документа внутри iframe для чтения его текста.
    body = browser.find_element(By.TAG_NAME, "body")

    time.sleep(3)
    # Проверяем наличие фрагмента в тексте, который возвращает WebElement.text.
    assert 'semper posuere integer et senectus justo curabitur.' in body.text
