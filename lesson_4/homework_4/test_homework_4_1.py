"""Тест изменения текста кнопки на странице Text Input с помощью Selenium."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    """Создать сессию Chrome с неявным ожиданием поиска элементов 10 секунд.

    После завершения использующего фикстуру теста закрыть браузер
    и завершить сессию WebDriver.

    Yields:
        selenium.webdriver.chrome.webdriver.WebDriver: Драйвер Chrome.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_button_text_changes(driver):
    """Проверить изменение текста кнопки на «ITCH» после ввода и нажатия.

    Args:
        driver (selenium.webdriver.chrome.webdriver.WebDriver): Драйвер
            из фикстуры pytest. В текущей реализации параметр заменяется
            новой сессией Chrome внутри теста.

    Raises:
        AssertionError: Если текст кнопки после нажатия отличается от «ITCH».
        selenium.common.exceptions.NoSuchElementException: Если поле ввода
            или кнопка не найдены на странице.
    """
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/textinput")
    input_field = driver.find_element(By.ID,"newButtonName")
    input_field.send_keys("ITCH")
    button = driver.find_element(By.ID, "updatingButton")
    button.click()
    assert button.text == 'ITCH'




