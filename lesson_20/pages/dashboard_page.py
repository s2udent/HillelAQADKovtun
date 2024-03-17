from lesson_20.pages.base_page import BasePage
from lesson_20.pages.category_page import CategoryPage
from lesson_20.core import DashboardLocators


class Dashboard(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DashboardLocators()

    def click_eva_beauty(self):
        self.click_on_element(self.locators.eva_beauty_banner)
        return CategoryPage(self.driver)

    def click_eva_pro(self):
        self.click_on_element(self.locators.eva_pro_banner)
        return CategoryPage(self.driver)

    def click_eva_premium(self):
        self.click_on_element(self.locators.eva_premium_banner)
        return CategoryPage(self.driver)

    def click_eva_health(self):
        self.click_on_element(self.locators.eva_health_banner)
        return CategoryPage(self.driver)

    def click_search_btn(self):
        self.click_on_element(self.locators.search_btn)
        return CategoryPage(self.driver)

    def hover_menu_perfumes(self):
        self.hover_element(self.locators.parjumerija_category)

    def click_spring_perfume(self):
        self.click_on_element(self.locators.spring_perfume)
        return CategoryPage(self.driver)
