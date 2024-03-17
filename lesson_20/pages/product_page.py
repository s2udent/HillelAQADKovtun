from lesson_20.pages.base_page import BasePage
from lesson_20.core import ProductLocators


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

    def continue_shopping_from_cart(self):
        self.click_on_element(self.locators.continue_shopping_cart_button)

    def verify_cart_is_not_shown(self):
        self.invisibility_of_cart(self.locators.cart_pop_up_header)





