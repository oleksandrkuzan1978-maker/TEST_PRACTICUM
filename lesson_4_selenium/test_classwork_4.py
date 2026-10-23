from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

CAT_MEMES = "https://suninjuly.github.io/cats.html#"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(CAT_MEMES)
    yield driver
    driver.quit()
#
# # Написать тест, который проверяет наличия теста "Cats album" возле иконки фото
# def test_find_all_cats(driver):
#     cats = driver.find_elements(By.CLASS_NAME, "box-shadow")
#     #print(f"\t\t{cats[3].text}")
#     for cat in cats:
#         print(cat.text, "\n")
#
#     # for cat in cats:
#     #     print(cat.__repr__())
#     assert 'Cats album' in cats[0].text
#
# # # Написать тест, который проверяет наличия текста “Cat memes” в заголовке страницы.
# # def test_find_cat_memes(driver):
# #     cat_memes = driver.find_element(By.CSS_SELECTOR, "body > main > section > div > h1")
# #     #print(f"\t\t{cats[3].text}")
# #     assert cat_memes.is_displayed() is True
# #
# #
# # def test_find_title(driver):
# #     title_text = driver.find_element(By.TAG_NAME, 'h1').text
# #     assert title_text == 'Cat memes'
#
#
# def test_find_album_cats(driver):
#     cats = driver.find_elements(By.CLASS_NAME, "box-shadow")
#     assert 'Cats album' in cats[0].text
#
# from selenium.webdriver.common.by import By
#
# def test_cats_album(driver):
#     element = driver.find_element(
#         By.CSS_SELECTOR,
#         ".navbar-brand strong"
#     )
#
#     assert element.text == "Cats album"


def test_login():
    driver = webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/login")
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    username_field = driver.find_element(By.ID, "password")
    username_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CLASS_NAME, "fa-sign-in")
    login_button.click()
    time.sleep(5)
    assert driver.find_element(
        By.XPATH,
        "//h4[text()='Welcome to the Secure Area. When you are done click logout below.']"
    )
    time.sleep(5)
