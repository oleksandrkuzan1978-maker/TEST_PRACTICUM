from time import sleep
from lesson_3.urls import CAT_MEMES
from lesson_3.locators import xpath_id_cat_bullet, xpath_name_cat_vova
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.expected_conditions import element_to_be_selected

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/forgot_password")
# form = driver.find_element(By.CSS_SELECTOR,"#forgot_password")
# print(form)
#
# element_by_xpath = driver.find_element(By.XPATH, '//*[@id="form_submit"]')
# print(element_by_xpath)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(CAT_MEMES)
    yield driver
    driver.quit()

def test_displayed_cat_bullet(driver):
    cat_bullet = driver.find_element(By.XPATH, xpath_id_cat_bullet)
    assert cat_bullet.is_displayed() is True

def test_displayed_cat_name_vova(driver):
    cat_vova = driver.find_element(By.XPATH, xpath_name_cat_vova)
    assert cat_vova.is_displayed() is True


