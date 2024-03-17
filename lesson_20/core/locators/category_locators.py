from .base_locators import BaseLocators


class CategoryLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.first_result_item = ('xpath', '//div[contains(@class, "product-card")][1]')
        self.parjumerija_category = ('xpath', '//div[@class="main-section"]//a[contains(@href,"parfjumerija")]')
        self.spring_perfume = ('xpath', '//div[@class="mega-menu__right-side"]//a[@href="/ua/q-vesennie-duhi/"]')
        self.calvin_clein_checkbox = ('xpath', '//input[@name="Calvin Klein"]/following-sibling::div[@class="sf-checkbox__checkmark"]')
        self.calvin_clein_checkbox_active = ('xpath', '//input[@name="Calvin Klein"]/following-sibling::div[contains(@class,"is-active")]')