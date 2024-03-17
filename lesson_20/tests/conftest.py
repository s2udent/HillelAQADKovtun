import pytest
from selenium.webdriver import Chrome
from lesson_20.pages.dashboard_page import Dashboard
from lesson_20.pages.product_page import Product
from lesson_20.pages.category_page import CategoryPage


@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def dashboard(driver):
    driver.get('https://eva.ua')
    yield Dashboard(driver)


@pytest.fixture
def glass_product(driver):
    driver.get('https://eva.ua/ua/pr31280/')
    yield Product(driver)


@pytest.fixture
def spring_perfume(driver):
    driver.get('https://eva.ua/ua/q-vesennie-duhi/')
    yield CategoryPage(driver)
