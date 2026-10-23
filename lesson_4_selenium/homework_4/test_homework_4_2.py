"""Тест атрибута alt третьего изображения на странице Loading images."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_third_image_alt():
    """Дождаться четырёх изображений в DOM и проверить alt третьего.

    Искать изображения внутри контейнера image-container в порядке DOM,
    ожидая появления каждого не более 10 секунд. Проверить, что атрибут
    alt третьего изображения равен «award». При успешном выполнении
    проверки закрыть браузер и завершить сессию WebDriver.

    Raises:
        selenium.common.exceptions.TimeoutException: Если очередное
            изображение не появилось в DOM за время ожидания.
        AssertionError: Если alt третьего изображения отличается от «award».
    """
    driver = webdriver.Chrome()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    wait = WebDriverWait(driver, 10)

    # image_ids = [
    #     "compass",
    #     "calendar",
    #     "award",
    #     "landscape"
    # ]
    #
    # images = []
    #
    # for image_id in image_ids:
    #     image = wait.until(
    #         EC.presence_of_element_located(
    #             (By.ID, image_id)
    #         )
    #     )
    #     images.append(image)
    images = []

    for i in range(1, 5):
        image = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"(//div[@id='image-container']/img)[{i}]")
            )
        )
        images.append(image)

    third_image = images[2]

    assert third_image.get_attribute("alt") == "award"

    driver.quit()