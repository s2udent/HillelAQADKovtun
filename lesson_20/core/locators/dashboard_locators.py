from .base_locators import BaseLocators


class DashboardLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.eva_beauty_banner = ('xpath', '//div[@class="categories-wrapper"]//a[contains(@href, "beauty")]')
        self.eva_pro_banner = ('xpath', '//div[@class="categories-wrapper"]//a[contains(@href, "professional-naja-kosmetika")]')
        self.eva_premium_banner = ('xpath', '//div[@class="categories-wrapper"]//a[contains(@href, "eva-premium")]')
        self.eva_health_banner = ('xpath', '//div[@class="categories-wrapper"]//a[contains(@href, "zdorove")]')
        self.parjumerija_category = ('xpath', '//div[@class="main-section"]//a[contains(@href,"parfjumerija")]')
        self.spring_perfume = ('xpath', '//div[@class="mega-menu__right-side"]//a[@href="/ua/q-vesennie-duhi/"]')
