from regular import regular_line
from regular import regular_digit


#No decorators
#No default constructor
#Int price???
class Item:
    def __init__(self, name: str, price: int, art: str, amount: int):
        self.__name = regular_line(name)
        self.__price = regular_digit(price)
        self.__art = str(regular_digit(art))
        self.__amount = regular_digit(amount)

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_art(self):
        return self.__art

    def get_amount(self):
        return self.__amount

    def set_name(self, name):
        self.__name = regular_line(name)

    def set_price(self, price):
        self.__price = regular_digit(price)

    def set_art(self, art):
        self.__art = str(regular_digit(art))

    def set_amount(self, amount):
        self.__amount = regular_digit(amount)


    def __eq__(self, other) -> bool:
        return self.__name == other.__name