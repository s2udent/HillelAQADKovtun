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

    def sort_asc(self):
        self.click_on_element(self.locators.sorting_ddl)
        self.click_on_element(self.locators.select_sort_asc)

    def sort_desc(self):
        self.click_on_element(self.locators.sorting_ddl)
        self.click_on_element(self.locators.select_sort_desc)

    def enter_brand_filter(self, text):
        self.enter_text(text, self.locators.brand_filter_search)

    def enter_country_filter(self, text):
        self.enter_text(text, self.locators.country_filter_search)

    def enter_main_accord(self, text):
        self.enter_text(text, self.locators.main_accords_filter_search)

    def get_name_of_brand_attribute(self):
        return self.get_attribute(self.locators.brand_filtered_item)

    def get_name_of_country_attribute(self):
        return self.get_attribute(self.locators.country_filtered_item)

    def get_name_of_main_accord_attribute(self):
        return self.get_attribute(self.locators.main_accords_filtered_item)

    def navigate_next_page(self):
        self.click_on_element(self.locators.navigate_next_page)

    def activate_filter_sale_goods(self):
        self.click_on_element(self.locators.sale_goods)

    def is_active_filter_sale_goods(self):
        self.wait_until_element_presence(self.locators.sale_goods_active)






