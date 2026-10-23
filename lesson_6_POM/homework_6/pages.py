"""Классы страниц SauceDemo для автоматических тестов покупки товаров."""

from decimal import Decimal

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Общие действия на страницах: ожидание элементов, нажатие и ввод текста."""
    def __init__(self, driver):
        """Сохраняет драйвер браузера и задаёт ожидание элементов до 10 секунд."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        """Ждёт доступности элемента для нажатия и нажимает на него."""
        self.wait.until(EC.element_to_be_clickable(locator)
                        , message=(f"На странице {type(self).__name__} элемент {locator} недоступен для нажатия"
        ),).click()

    def fill(self, locator, value):
        """Ждёт появления поля, очищает его и вводит указанное значение."""
        element = self.wait.until(EC.visibility_of_element_located(locator)
                                  , message=f"Не открылась страница {type(self).__name__}",)
        element.clear()
        element.send_keys(value)

# URL = "https://www.saucedemo.com/"
class LoginPage(BasePage):
    """Страница входа в SauceDemo с полями логина и пароля."""
    URL = "https://www.saucedemo.com/"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self):
        """Открывает страницу входа в браузере."""
        self.driver.get(self.URL)

    def login(self, username, password):
        """Вводит логин и пароль, затем нажимает кнопку входа."""
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)


class InventoryPage(BasePage):
    """Страница каталога с добавлением товаров в корзину."""
    PRODUCTS = {
        "Sauce Labs Backpack": (
            By.ID, "add-to-cart-sauce-labs-backpack"),
        "Sauce Labs Bolt T-Shirt": (
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        "Sauce Labs Onesie": (
            By.ID, "add-to-cart-sauce-labs-onesie"),
    }
    CART = (By.CLASS_NAME, "shopping_cart_link")

    def add_products(self, products):
        """Добавляет в корзину товары по названиям из переданного списка."""
        for product in products:
            self.click(self.PRODUCTS[product])

    def open_cart(self):
        """Нажимает на значок корзины и открывает её."""
        self.click(self.CART)

class CartPage(BasePage):
    """Страница корзины с переходом к оформлению заказа."""
    CHECKOUT = (By.ID, "checkout")

    def checkout(self):
        """Нажимает кнопку оформления заказа в корзине."""
        self.click(self.CHECKOUT)

class CheckoutInformationPage(BasePage):
    """Страница ввода имени, фамилии и почтового индекса покупателя."""
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")

    def fill_and_continue(self, first_name, last_name, postal_code):
        """Заполняет данные покупателя и переходит к проверке заказа."""
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE)
# <div class="inventory_item_price" data-test="inventory-item-price">$29.99</div>
class CheckoutOverviewPage(BasePage):
    """Страница проверки заказа с итоговой суммой к оплате."""
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def get_total(self):
        """Читает итоговую сумму со страницы и возвращает её как Decimal."""
        element = self.wait.until(EC.visibility_of_element_located(self.TOTAL)
                                  , message="На странице CheckoutOverviewPage не появилась итоговая сумма",)
        return Decimal(element.text.split("$", 1)[1].strip())



