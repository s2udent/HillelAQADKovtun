import time
def test_open_spring_perfume_from_base(dashboard):
    dashboard.hover_menu_perfumes()
    category = dashboard.click_spring_perfume()
    assert category.check_title('ᐈ Весняні парфуми — купити на EVA.UA @ Київ і Україна')


def test_select_kelvin_klein(spring_perfume):
    spring_perfume.click_kelvin_clein_check_box()
    spring_perfume.verify_active_checkbox_kelvin_clein()


def test_sorting_desc(spring_perfume):
    spring_perfume.sort_desc()
    assert spring_perfume.url_contains('sort=price.desc')


def test_sorting_asc(spring_perfume):
    spring_perfume.sort_asc()
    assert spring_perfume.url_contains('sort=price.asc')


def test_search_brand_filter(spring_perfume):
    spring_perfume.enter_brand_filter('Adidas')
    name = spring_perfume.get_name_of_brand_attribute()
    assert name == 'Adidas'


def test_search_country_filter(spring_perfume):
    spring_perfume.enter_country_filter('Україна')
    name = spring_perfume.get_name_of_country_attribute()
    assert name == 'Україна'


def test_search_main_accords(spring_perfume):
    spring_perfume.enter_main_accord('Хвойний')
    name = spring_perfume.get_name_of_main_accord_attribute()
    assert name == 'Хвойний'


def test_navigate_next_page(spring_perfume):
    spring_perfume.navigate_next_page()
    assert spring_perfume.url_contains('p=2')


def test_activate_sale_goods_filter(spring_perfume):
    spring_perfume.activate_filter_sale_goods()
    spring_perfume.is_active_filter_sale_goods()
