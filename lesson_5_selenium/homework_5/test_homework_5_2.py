"""Тест перетаскивания фотографии из галереи в корзину внутри iframe."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest


url = "https://www.globalsqa.com/demo-site/draganddrop/"

@pytest.fixture
def driver():
    """Создаёт Chrome, открывает страницу задания и передаёт драйвер тесту.

    После завершения теста закрывает браузер и завершает сессию WebDriver."""
    # Запускаем Chrome и создаём сессию для управления браузером.
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    # Задаём ожидание при поиске элементов; это не фиксированная пауза.
    driver.implicitly_wait(10)

    # Передаём драйвер тесту; код ниже выполнится при завершении фикстуры.
    yield driver
    # Закрываем все окна браузера и завершаем сессию WebDriver.
    driver.quit()


def test_drag_and_drop(driver):
    """Перетаскивает первую фотографию в корзину и проверяет количество карточек.

    Ожидается одна фотография в корзине и три фотографии в галерее."""
    # Находим iframe, в адресе которого есть photo-manager.
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe[src*='photo-manager']")
    # Переключаем поиск элементов на содержимое iframe.
    driver.switch_to.frame(iframe)

    # Выбираем первую карточку фотографии в галерее.
    photo = driver.find_element(By.XPATH, '//ul[@id="gallery"]/li[1]')
    # Находим корзину — область назначения для фотографии.
    trash = driver.find_element(By.ID, 'trash')
    #
    actions = ActionChains(driver)
    # Выполняем действия мыши; результат перемещения проверяем отдельно ниже.
    actions.drag_and_drop(photo, trash).perform()

    # Считаем найденные карточки в корзине; пустой список даёт 0.
    photos_in_trash = len(
        driver.find_elements(
            By.XPATH,
            "//div[@id='trash']//ul/li"
        )
    )

    # Считаем карточки, оставшиеся в исходной галерее.
    photos_in_gallery = len(
        driver.find_elements(
            By.XPATH,
            "//ul[@id='gallery']/li"
        )
    )

    # Проверяем, что в корзину переместилась одна фотография.
    assert photos_in_trash == 1
    # Проверяем, что из четырёх фотографий в галерее осталось три.
    assert photos_in_gallery == 3
