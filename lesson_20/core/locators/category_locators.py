from .base_locators import BaseLocators


class CategoryLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.first_result_item = ('xpath', '//div[contains(@class, "product-card")][1]')
        self.parjumerija_category = ('xpath', '//div[@class="main-section"]//a[contains(@href,"parfjumerija")]')
        self.spring_perfume = ('xpath', '//div[@class="mega-menu__right-side"]//a[@href="/ua/q-vesennie-duhi/"]')
        self.calvin_clein_checkbox =\
            ('xpath', '//input[@name="Calvin Klein"]/following-sibling::div[@class="sf-checkbox__checkmark"]')
        self.calvin_clein_checkbox_active = \
            ('xpath', '//input[@name="Calvin Klein"]/following-sibling::div[contains(@class,"is-active")]')
        self.sorting_ddl = ('xpath', '//div[@id="sfSelect"]')
        self.select_sort_asc = ('xpath', '//li[@id="price.asc"]')
        self.select_sort_desc = ('xpath', '//li[@id="price.desc"]')
        self.brand_filter_search = ('xpath', '//div[contains(@class,"o-filter-brand__search-filter")]//input')
        self.brand_filtered_item = ('xpath', '//div[@class="o-filter-brand__item"]//input')
        self.main_accords_filter_search = \
            ('xpath', '//div[@class="o-filter"]//span[contains(text(), "Основні акорди")]/..//input')
        self.main_accords_filtered_item = \
            ('xpath', '//div[@class="o-filter"]//span[contains(text(), "Основні акорди")]/..//input[@type="checkbox"]')
        self.country_filter_search = \
            ('xpath', '//div[@class="o-filter"]//span[contains(text(), "Країна виробництва")]/..//input')
        self.country_filtered_item = \
            ('xpath', '//div[@class="o-filter"]//span[contains(text(), "Країна виробництва")]/..//input[@type="checkbox"]')
        self.navigate_next_page = ('xpath', '//*[@id="product-list"]//button[contains(@class,"next")]')
        self.sale_goods = ('xpath', '//div[@class="o-filter-promo"]//div[@class="sf-checkbox__checkmark"]')
        self.sale_goods_active = ('xpath', '//div[@class="o-filter-promo"]//div[contains(@class,"checkmark--is-active")]')





