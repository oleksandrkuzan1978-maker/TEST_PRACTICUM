"""Тест вычисления математического выражения, заполнения формы и проверки alert."""

#. https://suninjuly.github.io/math.html
# 2. Вычислить математическое выражение
# ● Найти выражение на странице.
# ● Посчитать его значение.
# ● Ввести полученный результат в поле ввода.
# 3. Выбрать чекбокс
# ● Установить флажок "I'm the robot".
# 4. Выбрать радиокнопку
# ● Кликнуть по радио-кнопке "Robots rule".
# 5. Отправить форму
# ● Нажать на кнопку "Submit".
# 6. Проверить Alert
# ● Дождаться появления всплывающего окна (alert).
# ● Проверить, что текст alert содержит "Congrats, you've passed the task!"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import pytest
from time import sleep
import math


def calc(x):
    """Возвращает ln(abs(12 * sin(x))) в виде строки для ввода в поле формы.

    Аргумент x — текстовое представление целого числа; sin использует радианы."""
    return str(math.log(abs(12*math.sin(int(x)))))


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

def test_math_form(browser):
    """Проверяет решение математического задания и сообщение об успехе в alert."""
    url = 'https://suninjuly.github.io/math.html'
    # Открываем страницу с заданием в браузере из фикстуры.
    browser.get(url)
    # Получаем значение x со страницы для вычисления математического выражения.
    x_value = browser.find_element(By.ID, 'input_value')
    # Вычисляем ln(abs(12*sin(x))); calc возвращает результат в виде строки.
    result = calc(x_value.text)

    # Находим поле ответа, очищаем его и вводим вычисленное значение.
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.clear()
    answer_input.send_keys(result)

    # Устанавливаем флажок «I'm the robot».
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # Выбираем радиокнопку «Robots rule».
    robot_rule_radio = browser.find_element(By.ID, "robotsRule")
    robot_rule_radio.click()

    # Находим кнопку Submit и отправляем заполненную форму.
    submit_button = browser.find_element(By.CLASS_NAME, "btn-default")
    submit_button.click()
    # Ждём появления alert не более 10 секунд; при превышении времени тест упадёт.
    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    # Читаем текст всплывающего окна для проверки результата задания.
    alert_text = Alert(browser).text
    expected_substing = "Congrats, you've passed the task!"
    # Проверяем, что сообщение содержит ожидаемый текст об успешном выполнении.
    assert expected_substing in alert_text
    # Делаем фиксированную паузу на указанное число секунд.
    sleep(5)
    # Подтверждаем alert, чтобы закрыть всплывающее окно.
    alert.accept()
