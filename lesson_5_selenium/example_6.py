"""Учебный пример перетаскивания элемента в целевую область внутри iframe.

Сценарий выполняется непосредственно при запуске или импорте модуля."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import  time
# Запускаем Chrome и создаём сессию для управления браузером.
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")

# Находим iframe, внутри которого расположено демонстрационное поле.
iframe = driver.find_element(By.CLASS_NAME, 'demo-frame')
# Переключаем поиск элементов на содержимое iframe.
driver.switch_to.frame(iframe)

# Находим элемент, который нужно перетащить.
source = driver.find_element(By.ID, 'draggable')
# Находим область, которая принимает перетаскиваемый элемент.
target = driver.find_element(By.ID, 'droppable')

# Делаем фиксированную паузу на 2 секунды; готовность элементов не проверяется.
time.sleep(2)
actions = ActionChains(driver)
# Выполняем захват, перенос и отпускание элемента в целевой области.
actions.drag_and_drop(source, target).perform()
# Делаем фиксированную паузу на 2 секунды; готовность элементов не проверяется.
time.sleep(2)
