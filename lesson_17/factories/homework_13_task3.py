from dishes import Pasta, Risotto, Pizza


class OrderPart:

    def order_dish(self, dish_name):
        if dish_name == 'Pasta':
            return Pasta()
        elif dish_name == 'Risotto':
            return Risotto()
        elif dish_name == 'Pizza':
            return Pizza()
        else:
            raise Exception(f'Dish {dish_name} can not be cooked at this time')


restaurant1 = OrderPart()
order1 = restaurant1.order_dish('Pasta')
print(order1.cook_dish())
print(order1)
