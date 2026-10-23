from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_about_button(driver):
    driver.get("https://itcareerhub.de/ru")
    about_button = driver.find_element(By.LINK_TEXT, 'О нас')
    about_button.click()
    #time.sleep(3)
    about_company = driver.find_element(By.LINK_TEXT, 'О компании')
    print(about_company.text)
    assert about_company.text == 'О компании'


#
# driver.save_screenshot("./screenshot.png")
# time.sleep(3)

# driver.set_window_size(640, 460)
# time.sleep(3)
#
# driver.fullscreen_window()
# time.sleep(3)
#
# driver.minimize_window()
# time.sleep(3)

# driver.refresh()
# time.sleep(3)
#
# driver.get("https://www.berlin.de/")
# time.sleep(3)
#
# driver.back()
# time.sleep(3)
#
# driver.forward()