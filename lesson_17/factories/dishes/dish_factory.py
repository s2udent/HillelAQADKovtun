from abc import ABC, abstractmethod


class DishFactory(ABC):
    _dish_name = ''

    @abstractmethod
    def cook_dish(self):
        pass
