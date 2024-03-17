from lesson_20.pages.dashboard_page import Dashboard
from lesson_20.pages.base_page import BasePage


def test_go_to_eva_beauty(dashboard):
    dashboard.click_eva_beauty()
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



