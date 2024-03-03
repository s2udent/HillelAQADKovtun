import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lesson_15.homework_12 import Train, TraintCart, Passenger


@pytest.mark.smoke
def test_train_creation(train):
    assert train.current_station == 'Dnipro'


@pytest.mark.smoke
def test_passenger_creation(passenger1):
    assert passenger1.place == 1


@pytest.mark.smoke
def test_train_cart_creation(train_cart):
    assert train_cart.num == 1


@pytest.mark.regression
def test_train_len(full_train):
    assert len(full_train) == 1


@pytest.mark.unstable
@pytest.mark.regression
@pytest.mark.xfail(reason='Incorrect train cart order')
@pytest.mark.parametrize(
    'train_cart, exp_train_cart_num',
    [(TraintCart(1), 1), (TraintCart(2), 3)]
)
def test_train_parametrized(train, train_cart, exp_train_cart_num):
    train[train_cart.num] = train_cart
    assert train[train_cart.num].num == exp_train_cart_num


@pytest.mark.regression
@pytest.mark.parametrize(
    'passenger,exp_pas_name,exp_pas_dest,exp_pas_place',
    [(Passenger('Dima', 'Kyiv', 1), 'Dima', 'Kyiv', 1),
     (Passenger('Tolik', 'Lviv', 2), 'Tolik', 'Lviv', 2),
     (Passenger('John', 'Vinnitsya', 3), 'John', 'Vinnitsya', 3)]
)
def test_train_cart_parametrized(train_cart, passenger, exp_pas_name, exp_pas_dest, exp_pas_place):
    train_cart[passenger.place] = passenger
    assert train_cart[passenger.place].passenger_name == exp_pas_name
    assert train_cart[passenger.place].destination == exp_pas_dest
    assert train_cart[passenger.place].place == exp_pas_place


