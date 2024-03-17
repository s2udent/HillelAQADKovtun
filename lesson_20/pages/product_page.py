from lesson_20.pages.base_page import BasePage
from lesson_20.core import ProductLocators
from selenium.webdriver.support import expected_conditions as EC


class Product(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductLocators()

    def add_to_card(self):
        self.click_on_element(self.locators.add_to_cart)

    def select_quantity_2(self):
        self.click_on_element(self.locators.quantity_of_product_ddl)
        self.click_on_element(self.locators.select_quantyty_2)

    def get_quantity_of_product(self):
        element = self.wait_until_element_presence(self.locators.quantity_of_product_num)
        return int(element.text.strip())



