from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lesson_20.core import BaseLocators

class BasePage:

    def __init__(self, driver, wait_time=5):
        self.driver = driver
        self.web_driver_wait = WebDriverWait(driver, wait_time)
        self.locators = BaseLocators()

    def wait_until_element_presence(self, locator: tuple[str, str]):
        return self.web_driver_wait.until(EC.presence_of_element_located(locator))

    def click_on_element(self, locator):
        element = self.wait_until_element_presence(locator)
        element.click()

    def enter_text(self, text, locator):
        element = self.wait_until_element_presence(locator)
        element.send_keys(text)

    def check_title(self, title):
        return self.web_driver_wait.until(EC.title_is(title))

    def hover_element(self, locator):
        element = self.wait_until_element_presence(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def url_contains(self, text):
        return self.web_driver_wait.until(EC.url_contains(text))

    def invisibility_of_cart(self, locator):
        return self.web_driver_wait.until(EC.invisibility_of_element(locator))

    def get_attribute(self, locator, atr_type='name'):
        return self.wait_until_element_presence(locator).get_attribute(atr_type)

    def check_text_in_element(self, locator, text):
        return self.web_driver_wait.until(EC.text_to_be_present_in_element(locator, text))

    def check_text_in_cart_popup_header(self, text):
        return self.check_text_in_element(self.locators.cart_pop_up_header, text)

    def click_shipping_and_payment(self):
        self.click_on_element(self.locators.shipping_and_payment)

    def click_tracking(self):
        self.click_on_element(self.locators.tracking)

    def enter_text_to_search(self, text):
        self.enter_text(text, self.locators.search_field)

    def go_to_main_page(self):
        self.click_on_element(self.locators.main_page_logo)

    def go_to_mom_of_the_year(self):
        self.click_on_element(self.locators.mom_of_the_year)




