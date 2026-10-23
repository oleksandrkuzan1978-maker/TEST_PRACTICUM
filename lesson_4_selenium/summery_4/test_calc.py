
"""Проверка сложения на странице Slow Calculator с помощью Selenium."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest

@pytest.fixture
def driver():
    """Создать сессию Chrome с неявным ожиданием поиска элементов 10 секунд.

    После завершения теста закрыть браузер и завершить сессию WebDriver.

    Yields:
        selenium.webdriver.chrome.webdriver.WebDriver: Драйвер Chrome.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_calc(driver):
    """Проверить, что Slow Calculator вычисляет 7 + 8 и показывает 15.

    Установить задержку вычисления 10 секунд и после нажатия кнопки
    равенства ожидать появления результата не более 15 секунд.

    Args:
        driver: Драйвер Chrome, предоставленный фикстурой driver.
    """
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    delay = driver.find_element(By.ID, "delay")
    delay.clear()
    delay.send_keys("10")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()


    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), "15"
        )
    )

    result = driver.find_element(By.CLASS_NAME, "screen").text

    assert result == "15"


