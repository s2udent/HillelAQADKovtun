from lesson_20.pages.base_page import BasePage, Cookies, LocalStorage
from lesson_20.pages.category_page import CategoryPage
from lesson_20.core import DashboardLocators


class Dashboard(BasePage, Cookies, LocalStorage):

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

    def click_face_category(self):
        self.click_on_element(self.locators.face_cat)

    def click_hair_category(self):
        self.click_on_element(self.locators.hair_cat)

    def click_dermatokosmetika_category(self):
        self.click_on_element(self.locators.dermatokosmetika_cat)

    def click_prof_cosmetika_category(self):
        self.click_on_element(self.locators.prof_cosmetika_cat)

    def click_prem_category(self):
        self.click_on_element(self.locators.prem_cosmetika_cat)

    def click_health_category(self):
        self.click_on_element(self.locators.health_cat)

    def click_corea_category(self):
        self.click_on_element(self.locators.corea_cat)

    def click_badi_dobavki_category(self):
        self.click_on_element(self.locators.badi_dobavki)

    def click_nails_category(self):
        self.click_on_element(self.locators.nails_cat)


