"""Учебный пример раскрытия вложенного меню наведением указателя мыши."""

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from lesson_4.test_classwork_4 import driver

# Фикстура для WebDriver
# @pytest.fixture
# def browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()

def test_move():
    """Раскрывает вложенное меню наведением мыши и нажимает Secondary Action.

    Проверка assert подтверждает наличие объекта элемента, а не его видимость."""
    # Запускаем Chrome и создаём сессию для управления браузером.
    driver = webdriver.Chrome()
    driver.get("https://crossbrowsertesting.github.io/hover-menu.html")

    # Находим пункт меню по точному тексту ссылки.
    dropdown = driver.find_element(By.LINK_TEXT, "Dropdown")
    actions = ActionChains(driver)
    # Наводим мышь на Dropdown, чтобы раскрыть меню.
    actions.move_to_element(dropdown).perform()

    # Находим пункт, который раскрывает вложенное меню.
    secondary_menu = driver.find_element(By. LINK_TEXT, 'Secondary Menu')
    # Делаем фиксированную паузу на 2 секунды; готовность элементов не проверяется.
    sleep(2)
    # Наводим мышь на Secondary Menu, чтобы раскрыть следующий уровень.
    actions.move_to_element(secondary_menu).perform()
    secondery_action = driver.find_element(By. LINK_TEXT, 'Secondary Action')
    # Делаем фиксированную паузу на 3 секунды; готовность элементов не проверяется.
    sleep(3)
    # Проверяем наличие объекта WebElement; видимость эта проверка не проверяет.
    assert secondery_action

    # Нажимаем найденный пункт вложенного меню.
    secondery_action.click()
