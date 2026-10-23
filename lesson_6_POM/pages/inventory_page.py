from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_items(self):
        return self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

    def get_items_amount(self):
        return len(self.get_items())

    def all_items_are_displayed(self):
        return all(item.is_displayed() for item in self.get_items())

    def get_item_names(self):
        obj_list =  self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))
        return [item.text for item in obj_list]

    def all_items_name_are_displayed(self):
        return all(name.strip() != "" for name in self.get_item_names())

    def all_items_names_are_not_empty(self):
        return all(bool(name.strip()) for name in self.get_item_names())

    def all_items_names_contains_sause_labs(self):
        return all(name.startswith('Sause Labs') for name in self.get_item_names())





