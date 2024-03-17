
def test_add_to_cart_glasses_from_search(dashboard):
    dashboard.enter_text_to_search('Набір склянок')
    category = dashboard.click_search_btn()
    product_item = category.click_first_product()
    product_item.add_to_card()
    assert product_item.check_text_in_cart_popup_header('Товарів у кошику: 1')


def test_quantity_of_product(set_of_glasses):
    beginning_quantity = set_of_glasses.get_quantity_of_product()
    set_of_glasses.select_quantity_2()
    ending_quantity = set_of_glasses.get_quantity_of_product()
    assert ending_quantity == beginning_quantity+1
