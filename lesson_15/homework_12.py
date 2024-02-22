# Task 1
class Train:
    def __init__(self, name, current_station):
        self.__name = name
        self.__current_station = current_station
        self.__traincarts = {}

    def __len__(self):
        return len(self.__traincarts)

    @property
    def current_station(self):
        return self.__current_station

    @current_station.setter
    def current_station(self, station_name):
        self.__current_station = station_name

    def __setitem__(self, key, value):
        self.__traincarts[key] = value

    def __getitem__(self, item):
        return self.__traincarts[item]


class TraintCart:

    def __init__(self, num):
        self.num = num
        self.__place = {}

    def __str__(self):
        dict_to_str = ''
        for v in self.__place.values():
            dict_to_str += (f'"passanger_name": "{v.passenger_name}"\n'
                            f'"destination": "{v.destination}"\n'
                            f'"place": "{v.place}"\n')

        return (f'"traincart" : "{self.num}"\n'
                f'{dict_to_str}')

    def __len__(self):
        return len(self.__place)

    def __setitem__(self, key, value):
        self.__place[key] = value

    def __getitem__(self, item):
        return self.__place[item]


class Passenger:

    def __init__(self, passenger_name, destination, place):
        self.passenger_name = passenger_name
        self.destination = destination
        self.place = place


'''Train #1'''
kyiv_rahiv = Train('Kyiv-Rahiv', 'Kyiv')

'''Cart #1-2'''
train_cart1 = TraintCart(1)
train_cart2 = TraintCart(2)

'''Passengers #1-2'''
passenger_dima = Passenger('Dmytro Kovtun', 'Rahiv',  1)
passenger_dakota = Passenger('Dakota Johnson', 'Lviv', 2)

'''Passengers #3-4'''
passenger_tolik = Passenger('Tolik Bolik', 'Vinnitsya',  1)
passenger_masha = Passenger('Masha Nyasha', 'Zhitomir',  2)

'''Cart #1-2 joined Train #1'''
kyiv_rahiv[train_cart1.num] = train_cart1
kyiv_rahiv[train_cart2.num] = train_cart2

'''Passengers #1-2 joined Cart #1'''
train_cart1[passenger_dima.place] = passenger_dima
train_cart1[passenger_dakota.place] = passenger_dakota

'''Passengers #3-4 joined Cart #2'''
train_cart2[passenger_tolik.place] = passenger_tolik
train_cart2[passenger_masha.place] = passenger_masha

print(len(kyiv_rahiv), 'num of carts')
print(len(train_cart1), 'num of passengers in cart 1')
print(len(train_cart2), 'num of passengers in cart 2')
print()
print(train_cart1)
print(train_cart2)








