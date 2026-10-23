# <h6 data-v-7b563373="" data-v-c286b6e5="" class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module">Dashboard</h6>

"""Проверка входа в OrangeHRM и появления заголовка Dashboard."""
from os import waitstatus_to_exitcode



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    """Создать сессию Chrome для теста.

    После завершения использующего фикстуру теста закрыть браузер
    и завершить сессию WebDriver.

    Yields:
        selenium.webdriver.chrome.webdriver.WebDriver: Драйвер Chrome.
    """
    driver = webdriver.Chrome()

    yield driver
    driver.quit()


def test_login_to_orangehrm(driver):
    """Проверить вход в OrangeHRM с учетными данными Admin/admin123.

    Заполнить форму входа и отправить ее. Ожидать появления полей,
    доступности кнопки и текста Dashboard в заголовке h6, выделяя
    на каждое явное ожидание до 10 секунд.

    Args:
        driver: Драйвер Chrome, предоставленный фикстурой driver.
    """

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait = WebDriverWait(driver, 10)

    username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    username_field.send_keys("Admin")

    password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    password_field.send_keys("admin123")

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
    login_button.click()

    dashboard_header = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h6"), "Dashboard"))
    assert dashboard_header, "В заголовке нет текста 'Dashboard'"




