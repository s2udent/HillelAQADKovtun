
class BaseLocators:
    def __init__(self):
        self.shipping_and_payment = ('xpath', '//a[contains(@href, "oplata-dostavka")]')
        self.tracking = ('xpath', '//a[contains(@href, "tracking")]')
        self.search_field = ('xpath', '//input[@type="search"]')
        self.search_btn = ('xpath', '//div[@id="header"]//button[@type="submit"]')
        self.cart_pop_up_header = ('xpath', '//header[@class="modal__header"]//h2')
        self.main_page_logo = ('xpath', '//span[@class="a-logo"]/a[contains(@href,"/")]')
        self.mom_of_the_year = ('xpath', '//a[contains(text(), "Мама року")]')
