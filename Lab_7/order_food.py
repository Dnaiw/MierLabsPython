from order import Order
from item import Item
from datetime import datetime
from datetime import timedelta

class Order_food(Order):

    list_product = {"1": Item("Стейк из говядины", 250, "223614512", 1),
                    "2": Item("Суп грибной", 20, "221425512", 1),
                    "3": Item("Рис", 380, "227814512", 1),
                    "4": Item("Котлеты белорусские", 400, "221451912", 1),
                    "5": Item("Чай Премиум", 800, "213214512", 1)}


    def __str__(self):
        return ". продуктовый заказ " + Order.__str__(self)

    def __init__(self):
        print("\n")
        Order_food.menu()
        print("\n")
        Order.__init__(self) #supper()
        self.line = input("Выберите через пробел номера блюд, которые хотите заказать: ")
        for product in self.line.split():
            flag = True
            try:
                for i in self.list_consumer:
                    if i.get_name() == Order_food.list_product[product].get_name():
                        i.set_amount(i.get_amount() + 1)
                        flag = False
                        break
                if flag:
                    self.list_consumer.append(Item(Order_food.list_product[product].get_name(), Order_food.list_product[product].get_price(),
                                                   Order_food.list_product[product].get_art(), 1))
            except KeyError:
                print("Элемента ", product, " нет в нашем меню")

        self.all_price()

    @staticmethod
    def menu(): #print_menu
        for key in Order_food.list_product:
            print(key + ". " + Order_food.list_product[key].get_name() + " " + str(Order_food.list_product[key].get_price()))

    def products(self):
        print("_" * 60)
        Order.products(self)

    def delivery(self):
        print("Заказ зарегистрирован " + self.date_reg.strftime("%m/%d/%Y, %H:%M:%S"))

        if self.date_accept == 0 and self.date_reg + timedelta(minutes=1) < datetime.today():
            print("Заказ испортился и не доставлен!")
        elif self.date_accept != 0 and self.date_reg + timedelta(minutes=1) > date_accept: #missing self
            print("Заказ доствлен вовремя")
        elif self.date_accept == 0 and self.date_reg + timedelta(minutes=1) > datetime.today():
            print("Заказ не доставлен, но ещё свежий")
        else:
            print("Заказ доставлен, но товар испортился")

    @staticmethod
    def reset():

        print("Введите название новой позиции:")
        name = input()

        print("Введите цену: ")
        price = input()

        print("Введите артикул: ")
        art = input()

        Order_food.list_product[str(len(Order_food.list_product) + 1)] = Item(name, price, art, 1)
