from .base_locators import BaseLocators


class ProductLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.add_to_cart = ('xpath', '//div[@class="product__price-info"]//div[contains(@class,"add-to-cart")]/button')
        self.quantity_of_product_ddl = ('xpath', '//div[@class="product__price-info"]//div[contains(@class,"select-option")]/..')
        self.quantity_of_product_num = ('xpath', '//div[@class="product__price-info"]//div[contains(@class,"select-option")]')
        self.select_quantyty_2 = ('xpath', '//div[@class="sf-select__dropdown"]/ul[@aria-expanded="true"]/li[@id="2"]')