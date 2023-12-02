from datetime import datetime
from datetime import timedelta

from regular_exeption import RegularExeption
from regular import regular_line, regular_digit
from item import Item

class Order:
    NDS = 0.125
    list_product = dict()

    def __init__(self):
        self.name = input("Введите ваше имя: ") #Console input in conctructor????
        self.adress = input("Введите адрес: ")
        self.date_reg = datetime.today()
        self.date_accept = 0
        self.price = 0
        self.list_consumer = []
        for product in self.list_consumer: #List is always empty
            self.price += product.get_price()


    def __str__(self):
        if self.date_accept == 0:
            value = "Не доставлен"
        else:
            value = "Доставлен"

        return self.name + " " + self.adress + " " + self.date_reg.strftime("%m/%d/%Y, %H:%M:%S") + " " + value

    def equals(self, other) -> bool:
        for product in self.list_consumer:
            if product in other.list_consumer and self.list_consumer.count(product) == other.list_consumer.count(product):
                pass
            else:
                return False
            return True


    def products(self): #Should be print_products or return collection
        for product in self.list_consumer:
            print("_" * 60)
            print("Наименование: " + product.get_name())
            print("Количество в заказе: " + str(product.get_amount()))
            print("Цена: " + str(product.get_price()))
            print("Артикул: " +  product.get_art())
            print("_" * 60)
        print("ИТОГО:" + str(self.price))
        print("Из них НДС: " + str(self.NDS * self.price))
        print("_" * 60)

    def delivery(self):
        print("Заказ зарегистрирован " + self.date_reg.strftime("%m/%d/%Y, %H:%M:%S"))
        if self.date_accept != 0:
            print("Дата доставки: " + self.date_reg.strftime("%m/%d/%Y, %H:%M:%S"))
        else:
            print("Заказ ещё не доставлен")

    def accept(self):
        if self.date_accept == 0:
            self.date_accept = datetime.today()
            print("Статус изменён")
        else:
            print("Заказ уже был доставлен")

    def __sub__(self, other: str) -> bool:
        for i in range(len(self.list_consumer)):
            if self.list_consumer[i].get_name() == other:
                self.list_consumer.pop(i)
                print("Позиция успешно удалена\n")
                self.all_price()
                return True
        print("Такой позиции в заказе не было\n")
        return False


    def all_price(self): #Set/update all_price is better
        self.price = 0
        for i in self.list_consumer:
            self.price += i.get_price() * i.get_amount()

