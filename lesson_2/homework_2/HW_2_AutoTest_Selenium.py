import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


def test_go_to_page(driver):

    # Открываем сайт
    driver.get("https://itcareerhub.de/ru")
    time.sleep(3)

    # Принимаем cookies
    cookie_button = driver.find_element(
        By.XPATH,
        "//*[@id='rec1393944341']/div/div[1]/div[3]/div/button[1]/span"
    )
    time.sleep(3)
    cookie_button.click()
    time.sleep(2)

    # Находим ссылку "Способы оплаты"
    payment_methods = driver.find_element(
        By.LINK_TEXT,
        "Способы оплаты"
    )
    time.sleep(2)
    # Нажимаем
    payment_methods.click()
    time.sleep(2)

    # Находим саму секцию
    payment_section = driver.find_element(
        By.ID,
        "rec1921734713"
    )

    # Проверяем, что секция отображается
    assert payment_section.is_displayed()

    # Делаем скриншот именно секции
    payment_section.screenshot(
        "./lesson_2/homework_2/screenshot.png"
    )
    driver.save_screenshot("./lesson_2/homework_2/screenshot.png")

    print('Скриншот готов')
    time.sleep(2)



