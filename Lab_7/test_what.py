import pytest
import pickle
from order import Order
from order_food import Order_food
from order_item import Order_item
from item import Item

@pytest.fixture()
def hz():
    return "!!!!!!!!!!"

@pytest.fixture(autouse=True)
def clean():
    print("Я здесь ", end="")

@pytest.mark.parametrize("test_value,expected", [("1 2 3", 650), ("1 2 4 5", 1470), ("1", 250), ("77 45 23", 0)])
def test_2(monkeypatch, test_value, expected, hz):
    def m(*args):
        pass
    print(hz)
    inputs = iter(["You", "Here", test_value])
    monkeypatch.setattr("builtins.input", lambda _:next(inputs))
    monkeypatch.setattr("order_food.Order_food.menu", m)
    monkeypatch.setattr("builtins.print", m)
    m = Order_food()
    assert m.price == expected

@pytest.mark.parametrize("test_value,expected", [("1 2 3", 650), ("1 2 3 5", 1450), ("77 45 23", 0)])
def test_3(monkeypatch, test_value, expected):
    def m(*args):
        pass

    inputs = iter(["You", "Here", test_value])
    monkeypatch.setattr("builtins.input", lambda _:next(inputs))
    monkeypatch.setattr("order_item.Order_item.menu", m)
    monkeypatch.setattr("builtins.print", m)
    m = Order_item()
    assert m.price == expected

