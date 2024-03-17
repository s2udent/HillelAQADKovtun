
def test_open_spring_perfume_from_base(dashboard):
    dashboard.hover_menu_perfumes()
    category = dashboard.click_spring_perfume()
    assert category.check_title('ᐈ Весняні парфуми — купити на EVA.UA @ Київ і Україна')


def test_select_kelvin_klein(spring_perfume):
    spring_perfume.click_kelvin_clein_check_box()
    spring_perfume.verify_active_checkbox_kelvin_clein()

