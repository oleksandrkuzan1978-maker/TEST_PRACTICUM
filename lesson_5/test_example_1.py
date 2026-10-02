"""Тест заполнения большой формы и проверки сообщения об успехе в alert."""

##1. http://suninjuly.github.io/huge_form.html
#2. Заполнить все поля ввода
#● Найти все input-поля типа text внутри формы.
#● Ввести в каждое поле значение "Hello".
#3. Нажать кнопку Submit
#● Найти кнопку с классом btn btn-default.
#● Нажать на неё.
#4. Дождаться появления Alert
#● Переключиться на всплывающее окно (alert).
#● Проверить текст Alert
#● Получить текст из alert.
#● Убедиться, что он содержит строку "Congrats, you've passed the task!".


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import pytest
from time import sleep

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

def test_fill_form_check_alert(browser):
    """Проверяет заполнение полей формы и сообщение об успехе в alert."""
    url = 'http://suninjuly.github.io/huge_form.html'
    # Открываем страницу с заданием в браузере из фикстуры.
    browser.get(url)
    # Находим все элементы input на странице для последующего заполнения.
    input_fields = browser.find_elements(By.TAG_NAME, "input")
    # Очищаем каждое найденное поле и вводим одинаковое значение Hello.
    for field in input_fields:
        field.clear()
        field.send_keys("Hello")
    # Находим кнопку Submit и отправляем заполненную форму.
    submit_button = browser.find_element(By.CLASS_NAME, "btn-default")
    submit_button.click()

    # Делаем фиксированную паузу на указанное число секунд.
    sleep(3)

    # Ждём появления alert не более 10 секунд; при превышении времени тест упадёт.
    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    #alert_text = Alert(browser).text
    # Читаем текст всплывающего окна для проверки результата задания.
    alert_text = browser.switch_to.alert.text
    expected_alert_text = "Congrats, you've passed the task!"
    # Проверяем, что сообщение содержит ожидаемый текст об успешном выполнении.
    assert expected_alert_text in alert_text
    # Делаем фиксированную паузу на указанное число секунд.
    sleep(3)
    # Подтверждаем alert, чтобы закрыть всплывающее окно.
    alert.accept()
