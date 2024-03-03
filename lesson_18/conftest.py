import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lesson_15.homework_12 import Train, TraintCart,Passenger


@pytest.fixture
def train():
    print('The train is agreed and connected')
    yield Train('Dnipro-Lviv', 'Dnipro')


@pytest.fixture
def passenger1():
    yield Passenger('Test Passenger', 'Test destination', 1)

@pytest.fixture
def passenger2():
    yield Passenger('Dima Passenger', 'Vinnitsya', 2)


@pytest.fixture
def train_cart():
    yield TraintCart(1)


@pytest.fixture
def full_train(train, train_cart, passenger1, passenger2):
    train[train_cart.num] = train_cart
    train_cart[passenger1.place] = passenger1
    train_cart[passenger2.place] = passenger2
    yield train


@pytest.fixture
def parametrized_train():
    def _train(train_name, train_station):
        return Train(train_name, train_station)
    return _train


@pytest.fixture
def parametrized_train_cart():
    def _passenger(pas_name, pas_dest, pas_place):
        return Passenger(pas_name, pas_dest, pas_place)
    return _passenger

