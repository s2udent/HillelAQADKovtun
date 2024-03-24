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
        self.face_cat = ('xpath', '//div[@class="mega-menu__left-side"]//a[contains(@href,"lico")]')
        self.hair_cat = ('xpath', '//div[@class="mega-menu__left-side"]//a[contains(@href,"volosy")]')
        self.dermatokosmetika_cat = ('xpath', '//div[@class="mega-menu__left-side"]//a[contains(@href,"dermatokosmetika")]')
        self.prof_cosmetika_cat = ('xpath', '//div[@class="mega-menu__left-side"]//a[contains(@href,"professional-naja-kosmetika")]')
        self.prem_cosmetika_cat = ('xpath', '//div[@class="mega-menu__left-side"]//a[contains(@href,"eva-premium")]')
        self.health_cat = ('xpath', '//div[@class="mega-menu__left-side"]//a[contains(@href,"zdorove")]')
        self.badi_dobavki = ('xpath', '//div[@class="mega-menu__left-side"]//a[contains(@href,"bady-i-pischevye-dobavki")]')
        self.corea_cat = ('xpath', '//div[@class="mega-menu__left-side"]//a[contains(@href,"koreja")]')
        self.nails_cat = ('xpath', '//div[@class="mega-menu__left-side"]//a[contains(@href,"nogti")]')





perfumes_cat = ('xpath', '//div[@class="main-section"]//a[contains(@href,"parfjumerija")]')
perfumes_sub_categories = [
    ('xpath', '//a[@href="/ua/217-12609-12612/zhidkoe-mylo-parfjumirovannoe/"]'),
    ('xpath', '//a[@href="/ua/217-12609-12616/maslo-tela-parfjumirovannoe/"]'),
    ('xpath', '//a[@href="/ua/217-12609-12615/loson-tela-parfjumirovannyj/"]')]

makeup_cat = ('xpath', '//div[@class="main-section"]//a[contains(@href,"kosmetika-dekorativnaja")]')
makeup_sub_cat = [
    ('xpath', '//a[@href="/ua/299-302-303/tush-resnic/"]'),
    ('xpath', '//a[@href="/ua/299-302-304/karandashi-kontura-glaz/"]'),
    ('xpath', '//a[@href="/ua/299-302-306/podvodka-glaz/"]')]

