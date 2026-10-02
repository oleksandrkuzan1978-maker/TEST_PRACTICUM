"""Учебный пример открытия новой вкладки и переключения между вкладками Chrome.

Сценарий выполняется непосредственно при запуске или импорте модуля."""

from tokenize import tabsize

from selenium import webdriver

# Запускаем Chrome и создаём сессию для управления браузером.
driver = webdriver.Chrome()
driver.get("https://example.com")

# Открываем новую вкладку
driver.execute_script("window.open('https://google.com', '_blank');")

# Выводим список всех вкладок
#print(driver.window_handles)

# Получаем идентификаторы открытых окон и вкладок.
tabs = driver.window_handles
print(tabs)

# Выводим идентификатор вкладки, которой сейчас управляет WebDriver.
print(driver.current_window_handle)


# Переключаем управление на вторую вкладку из полученного списка.
driver.switch_to.window(tabs[1])
# Выводим идентификатор вкладки, которой сейчас управляет WebDriver.
print(driver.current_window_handle)
# 825E2F29183AD53A726D94B6E9B127C1


# Возвращаем управление первой вкладке.
driver.switch_to.window(tabs[0])
# Выводим идентификатор вкладки, которой сейчас управляет WebDriver.
print(driver.current_window_handle)
