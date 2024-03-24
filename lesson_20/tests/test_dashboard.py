import pytest
from lesson_20.core.locators.dashboard_locators import perfumes_cat, perfumes_sub_categories, makeup_cat, makeup_sub_cat
from lesson_20.pages.dashboard_page import Dashboard
from lesson_20.pages.base_page import BasePage


def test_go_to_eva_beauty(dashboard):
    dashboard.click_eva_beauty()
    print(dashboard.get_cookies())
    print(dashboard.get_value_from_local_storage())
    assert dashboard.check_title('EVA Beauty — твій простір краси')


def test_go_to_evapro(dashboard):
    dashboard.click_eva_pro()
    assert dashboard.check_title('ᐈ ПРОФЕСІЙНА Косметика — купити на EVA.UA @ Київ і Україна')


def test_go_to_eva_premium(dashboard):
    dashboard.click_eva_premium()
    assert dashboard.check_title('ᐈ EVA PREMIUM — купити преміум косметику та парфумерію на EVA.UA @ Київ і Україна')


def test_go_to_eva_health(dashboard):
    dashboard.click_eva_health()
    assert dashboard.check_title("ᐈ Товари для ЗДОРОВ'Я та КРАСИ — купити на EVA.UA @ Київ і Україна")


def test_go_to_shipping_and_payment(dashboard):
    dashboard.click_shipping_and_payment()
    assert dashboard.check_title('Доставка в інтернет-магазині EVA.UA')


def test_go_to_tracking(dashboard):
    dashboard.click_tracking()
    assert dashboard.check_title('Відстежити власне замовлення на EVA.UA')


def test_open_mom_of_the_year(dashboard):
    dashboard.go_to_mom_of_the_year()
    assert dashboard.check_title('Мама року - Головна')


def test_face_category(dashboard):
    dashboard.click_face_category()
    assert dashboard.title_contains('Косметика для ОБЛИЧЧЯ')


def test_hair_category(dashboard):
    dashboard.click_hair_category()
    assert dashboard.title_contains('Косметика для ВОЛОССЯ')


def test_dermatokosmetika_category(dashboard):
    dashboard.click_dermatokosmetika_category()
    assert dashboard.title_contains('ДЕРМАТОКОСМЕТИКА')


def test_prof_category(dashboard):
    dashboard.click_prof_cosmetika_category()
    assert dashboard.title_contains('ПРОФЕСІЙНА Косметика')


def test_premium_category(dashboard):
    dashboard.click_prem_category()
    assert dashboard.title_contains('EVA PREMIUM — купити преміум косметику')


def test_health_category(dashboard):
    dashboard.click_health_category()
    assert dashboard.title_contains("Товари для ЗДОРОВ'Я та КРАСИ")


def test_badi_dobavki_category(dashboard):
    dashboard.click_badi_dobavki_category()
    assert dashboard.title_contains('БАДи — купити дієтичні харчові добавки')


def test_corea_category(dashboard):
    dashboard.click_corea_category()
    assert dashboard.title_contains('КОРЕЙСЬКА КОСМЕТИКА')


def test_nails_category(dashboard):
    dashboard.click_nails_category()
    assert dashboard.title_contains('КОСМЕТИКА для НІГТІВ')


@pytest.mark.parametrize('category,list_of_sub_categories',
                         [(perfumes_cat, perfumes_sub_categories), (makeup_cat, makeup_sub_cat)])
def test_perfume_category_items(dashboard, category, list_of_sub_categories):
    dashboard.check_items_in_category_menu(category, list_of_sub_categories)



