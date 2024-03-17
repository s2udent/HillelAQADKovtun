from lesson_20.pages.base_page import BasePage
from lesson_20.pages.product_page import Product
from lesson_20.core import CategoryLocators


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoryLocators()

    def click_first_product(self):
        self.click_on_element(self.locators.first_result_item)
        return Product(self.driver)

    def click_kelvin_clein_check_box(self):
        self.click_on_element(self.locators.calvin_clein_checkbox)

    def verify_active_checkbox_kelvin_clein(self):
        self.wait_until_element_presence(self.locators.calvin_clein_checkbox_active)




