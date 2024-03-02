from lesson_17.factories.dishes.dish_factory import DishFactory


class Pasta(DishFactory):
    _dish_name = 'Pasta'

    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"I'm a {self._dish_name} dish"

    def cook_dish(self):
        return f'Cooking your {self._dish_name}'