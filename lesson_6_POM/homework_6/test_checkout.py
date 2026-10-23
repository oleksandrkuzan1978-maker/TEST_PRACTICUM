"""Тест итоговой суммы заказа из трёх товаров в SauceDemo."""

from decimal import Decimal

import pytest
from selenium import webdriver
from variables import Var
from pages import (
    LoginPage,
    InventoryPage,
    CartPage,
    CheckoutInformationPage,
    CheckoutOverviewPage,
)

@pytest.fixture
def driver():
    """Запускает Chrome и разворачивает окно. После теста закрывает браузер."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_checkout_total(driver):
    """Проверяет, что сумма заказа из трёх выбранных товаров равна 58.29 доллара."""

    login = LoginPage(driver)
    login.open()
    login.login(Var.USERNAME, Var.PASSWORD)

    inventory = InventoryPage(driver)
    inventory.add_products(Var.PRODS)
    inventory.open_cart()

    CartPage(driver).checkout()

    CheckoutInformationPage(driver).fill_and_continue(**Var.CHECKOUT_DATA)

    total = CheckoutOverviewPage(driver).get_total()

    assert total == Decimal(Var.SUMA), f"Ожидалась сумма ${Var.SUMA}, получена ${total}"

