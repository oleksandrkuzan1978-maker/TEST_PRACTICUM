"""Тест решения математического задания в новой вкладке и проверки alert."""

#1. Открыть страницу: http://suninjuly.github.io/redirect_accept.html.
# 2. Кликнуть по кнопке, которая открывает новую вкладку.
# 3. Определить идентификатор новой вкладки и переключиться на неё.
# 4. Вычислить математическое выражение ln(abs(12*sin(x))).
# 5. Ввести результат в поле ввода.
# 6. Нажать кнопку Submit.
# 7. Проверить текст во всплывающем alert.
import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Фикстура для WebDriver
@pytest.fixture
def browser():
    """Создаёт Chrome и передаёт его тесту через yield.

    После завершения теста закрывает браузер и завершает сессию WebDriver."""
    # Запускаем Chrome и создаём сессию для управления браузером.
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Передаём драйвер тесту; код ниже выполнится при завершении фикстуры.
    yield driver
    # Закрываем все окна браузера и завершаем сессию WebDriver.
    driver.quit()

# Функция для вычисления выражения
def calc(x):
    """Возвращает ln(abs(12 * sin(x))) в виде строки для ввода в поле формы.

    Аргумент x — текстовое представление целого числа; sin использует радианы."""
    return str(math.log(abs(12 * math.sin(int(x)))))

def test_redirect_and_math(browser):
    """Проверяет переход в новую вкладку, решение задания и сообщение в alert."""
    url = 'http://suninjuly.github.io/redirect_accept.html'
    # Открываем страницу с заданием в браузере из фикстуры.
    browser.get(url)
    # Делаем фиксированную паузу на указанное число секунд.
    time.sleep(5)
    # Нажимаем кнопку, которая открывает страницу задания в новой вкладке.
    button = browser.find_element(By.CLASS_NAME, "trollface")
    button.click()

    # Берём идентификатор второй вкладки и переключаем WebDriver на неё.
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    # Получаем значение x со страницы для вычисления математического выражения.
    x_value = browser.find_element(By.ID, 'input_value').text
    # Вычисляем ln(abs(12*sin(x))); calc возвращает результат в виде строки.
    result = calc(x_value)

    # Находим поле ответа в новой вкладке и вводим вычисленное значение.
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)

    # Нажимаем Submit для отправки вычисленного ответа.
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    # Ждём появления alert не более 10 секунд; при превышении времени тест упадёт.
    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    # Читаем текст всплывающего окна для проверки результата задания.
    alert_text = Alert(browser).text
    expected_alert_text = "Congrats, you've passed the task!"
    # Проверяем, что сообщение содержит ожидаемый текст об успешном выполнении.
    assert expected_alert_text in alert_text
    # Делаем фиксированную паузу на указанное число секунд.
    time.sleep(5)
    # Подтверждаем alert, чтобы закрыть всплывающее окно.
    alert.accept()
