import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

URL = "https://itcareerhub.de/ru"

@pytest.fixture
def driver():
    """Откройте русскоязычную главную страницу в Chrome для одного теста.

    После завершения теста закройте браузер и завершите сессию WebDriver.

    Yields:
        selenium.webdriver.chrome.webdriver.WebDriver: Драйвер браузера
            с открытой страницей URL.

    Raises:
        selenium.common.exceptions.WebDriverException: Если не удалось
            запустить браузер, открыть страницу или завершить сессию.
    """
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver

    driver.quit()


def test_logo_is_displayed(driver):
    """Проверьте видимость логотипа IT Career Hub.

    Args:
        driver (selenium.webdriver.remote.webdriver.WebDriver): Драйвер
            браузера, предоставленный фикстурой driver.

    Raises:
        AssertionError: Если проверяемый элемент не отображается.
        selenium.common.exceptions.NoSuchElementException: Если нужный
            для проверки элемент не найден.
    """
    logo = driver.find_element( By.XPATH, '//img[@alt="IT Career Hub"]')
    assert logo.is_displayed()



def check_span_links_displayed(driver, link):
    """Верните признак видимости ссылки с указанным текстом внутри span.

    Поиск использует первое совпадение и точное сравнение текста span
    после нормализации пробелов средствами XPath.

    Args:
        driver (selenium.webdriver.remote.webdriver.WebDriver): Драйвер
            браузера с открытой проверяемой страницей.
        link (str): Текст вложенного span без одинарных кавычек,
            поскольку значение напрямую подставляется в XPath.

    Returns:
        bool: True, если найденная ссылка видима, иначе False.

    Raises:
        selenium.common.exceptions.NoSuchElementException: Если ссылка
            с указанным текстом не найдена.
    """
    span_link = driver.find_element(
        By.XPATH,
        f"//a[.//span[normalize-space()='{link}']]"
    )

    return span_link.is_displayed()


def check_a_links(driver, link):
    """Найдите первую ссылку с указанным текстом.

    Текст элемента a сравнивается точно после нормализации пробелов
    средствами XPath. Видимость найденного элемента не проверяется.

    Args:
        driver (selenium.webdriver.remote.webdriver.WebDriver): Драйвер
            браузера с открытой проверяемой страницей.
        link (str): Текст ссылки без одинарных кавычек, поскольку
            значение напрямую подставляется в XPath.

    Returns:
        selenium.webdriver.remote.webelement.WebElement: Найденная ссылка.

    Raises:
        selenium.common.exceptions.NoSuchElementException: Если ссылка
            с указанным текстом не найдена.
    """
    a_link = driver.find_element(
        By.XPATH,
        f"//a[normalize-space()='{link}']"
    )

    return a_link
#

def test_programs_displayed(driver):
    """Проверьте видимость ссылки «Программы».

    Args:
        driver (selenium.webdriver.remote.webdriver.WebDriver): Драйвер
            браузера, предоставленный фикстурой driver.

    Raises:
        AssertionError: Если проверяемый элемент не отображается.
        selenium.common.exceptions.NoSuchElementException: Если нужный
            для проверки элемент не найден.
    """
    assert check_span_links_displayed(driver, "Программы") is True


def test_pay_methods_displayed(driver):
    """Проверьте видимость ссылки «Способы оплаты».

    Args:
        driver (selenium.webdriver.remote.webdriver.WebDriver): Драйвер
            браузера, предоставленный фикстурой driver.

    Raises:
        AssertionError: Если проверяемый элемент не отображается.
        selenium.common.exceptions.NoSuchElementException: Если нужный
            для проверки элемент не найден.
    """
    assert check_span_links_displayed(driver, "Способы оплаты") is True


def test_reviews_displayed(driver):
    """Проверьте видимость ссылки «Отзывы».

    Args:
        driver (selenium.webdriver.remote.webdriver.WebDriver): Драйвер
            браузера, предоставленный фикстурой driver.

    Raises:
        AssertionError: Если проверяемый элемент не отображается.
        selenium.common.exceptions.NoSuchElementException: Если нужный
            для проверки элемент не найден.
    """
    assert check_span_links_displayed(driver, "Отзывы") is True


def test_vlog_displayed(driver):
    """Проверьте видимость ссылки «Блог».

    Args:
        driver (selenium.webdriver.remote.webdriver.WebDriver): Драйвер
            браузера, предоставленный фикстурой driver.

    Raises:
        AssertionError: Если проверяемый элемент не отображается.
        selenium.common.exceptions.NoSuchElementException: Если нужный
            для проверки элемент не найден.
    """
    assert check_span_links_displayed(driver, "Блог") is True


def test_ru_displayed(driver):
    """Проверьте видимость ссылки выбора русского языка «ru».

    Args:
        driver (selenium.webdriver.remote.webdriver.WebDriver): Драйвер
            браузера, предоставленный фикстурой driver.

    Raises:
        AssertionError: Если проверяемый элемент не отображается.
        selenium.common.exceptions.NoSuchElementException: Если нужный
            для проверки элемент не найден.
    """
    assert check_a_links(driver, "ru").is_displayed() is True


def test_de_displayed(driver):
    """Проверьте видимость ссылки выбора немецкого языка «de».

    Args:
        driver (selenium.webdriver.remote.webdriver.WebDriver): Драйвер
            браузера, предоставленный фикстурой driver.

    Raises:
        AssertionError: Если проверяемый элемент не отображается.
        selenium.common.exceptions.NoSuchElementException: Если нужный
            для проверки элемент не найден.
    """
    assert check_a_links(driver, "de").is_displayed() is True


def test_contacts_displayed(driver):
    """Проверьте переход к контактам и открытие формы карьерной консультации.

    Откройте меню, перейдите по ссылке «Контакты» и проверьте адрес
    страницы, заголовок и кнопку «ОБРАТНЫЙ ЗВОНОК». Нажмите кнопку
    и проверьте видимость текста приглашения на карьерную консультацию.

    Args:
        driver (selenium.webdriver.remote.webdriver.WebDriver): Драйвер
            браузера, предоставленный фикстурой driver.

    Raises:
        AssertionError: Если ожидаемый элемент не отображается или
            адрес страницы не начинается с URL раздела контактов.
        selenium.common.exceptions.NoSuchElementException: Если нужный
            для проверки элемент не найден.
    """
    about_us = driver.find_element(By.XPATH,"//a[.//span[normalize-space()='О нас']]")
    about_us.click()
    sleep(2)
    contacts = check_a_links(driver, "Контакты")
    assert contacts.is_displayed() is True
    contacts.click()
    sleep(5)

    assert driver.current_url.startswith("https://itcareerhub.de/ru/contact-us")
    # # Поиск элемента по части текста
    screen = driver.find_element(By.XPATH, "//h1[contains(., 'Контакты')]")
    assert screen.is_displayed() is True
    # проверка отображения кнопки "Обратный звонок"
    callback = driver.find_element(
        By.XPATH,
        "//a[.//span[normalize-space()='ОБРАТНЫЙ ЗВОНОК']]"
    )
    assert callback.is_displayed() is True
    # клик на кнопку "обратный звонок"
    callback.click()
    sleep(2)
    # Проверка, что надпись “Запишитесь на бесплатную карьерную консультацию” отображается во всплывающем окне
    consultation = driver.find_element(By.XPATH
                                       , "//*[contains(., 'Запишитесь на') and contains(., 'карьерную консультацию')]")
    assert consultation.is_displayed() is True



