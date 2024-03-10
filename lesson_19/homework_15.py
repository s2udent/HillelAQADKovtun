from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from lesson_19 import locators


def test_open_contact_page():
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://eva.ua/')
    oplata_dostavka_btn = driver.find_element(By.XPATH, locators.oplata_dostavka_btn)
    oplata_dostavka_btn.click()
    assert EC.title_is('Доставка в інтернет-магазині EVA.UA')
    '''через driver.title не встигає завантажитись сторінка і assert падає'''
    #assert driver.title == 'Доставка в інтернет-магазині EVA.UA'


def test_find_glass():
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://eva.ua/')
    search_filed = driver.find_element(By.XPATH, locators.search_field)
    search_filed.send_keys('Набір склянок')
    search_button = driver.find_element(By.XPATH, locators.search_btn)
    search_button.click()
    driver.implicitly_wait(3)
    first_search_result = driver.find_element(By.XPATH, locators.first_search_result)
    first_search_result.click()
    assert 'Набір склянок' in driver.title


def test_add_to_cart_from_results():
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://eva.ua/')
    left_menu = driver.find_element(By.XPATH, locators.left_menu)
    hover_on_parfjumerija = ActionChains(driver).move_to_element(left_menu)
    hover_on_parfjumerija.perform()
    gel_dusha_menu_item = driver.find_element(By.XPATH, locators.gel_dusha_menu_item)
    click_on_gel_dusha_menu_item = ActionChains(driver).click(gel_dusha_menu_item)
    click_on_gel_dusha_menu_item.perform()
    driver.implicitly_wait(5)
    add_to_cart_button = driver.find_element(By.XPATH, locators.add_to_cart_btn_from_results)
    add_to_cart_button.click()
    driver.implicitly_wait(5)
    assert EC.text_to_be_present_in_element(locators.cart_pop_up_header, 'Товарів у кошику: 1')
    '''текст спочатку "Кошик порожній", потім підвантажується товар'''


def test_second_page_of_popular_promo():
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://eva.ua/')
    see_popular_promo = driver.find_element(By.XPATH, locators.see_popular_promo)
    see_popular_promo.click()
    driver.implicitly_wait(5)
    second_page_btn = driver.find_element(By.XPATH, locators.second_page_btn)
    second_page_btn.click()
    assert EC.url_contains('p=2')


def test_sort_asc():
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://eva.ua/')
    spring_parf_btn = driver.find_element(By.XPATH, locators.spring_parf_btn)
    spring_parf_btn.click()
    driver.implicitly_wait(5)
    sorting_ddl = driver.find_element(By.XPATH, locators.sorting_ddl)
    sorting_ddl.click()
    sort_asc = driver.find_element(By.XPATH, locators.sort_asc)
    sort_asc.click()
    assert EC.url_contains('sort=price.asc')









