from order import Order
from item import Item

class Order_item(Order):

    def __str__(self):
        return ". cтандартный заказ " + Order.__str__(self)

    list_product = {"1": Item("Холодильник", 250, "2236142", 1), #why not int keys
                    "2": Item("Кофеварка", 20, "2234512", 1),
                    "3": Item("Пылесос", 380, "2234512", 1),
                    "4": Item("Часы", 400, "2236145", 1),
                    "5": Item("Ноутбук", 800, "3614512", 1)}

    def __init__(self):
        print("\n")
        Order_item.menu()
        print("\n")#Not printing and reading in constructor!!!
        Order.__init__(self)
        self.line = input("Выберите через пробел номера блюд, которые хотите заказать: ")
        for product in self.line.split():
            flag = True
            try:
                for i in self.list_consumer:
                    if i.get_name() == Order_item.list_product[product].get_name():
                        i.set_amount(i.get_amount() + 1)
                        flag = False
                        break
                if flag: # could get the item only 1 time and create constructor(product)
                    self.list_consumer.append(
                        Item(Order_item.list_product[product].get_name(), Order_item.list_product[product].get_price(),
                             Order_item.list_product[product].get_art(), 1))
            except KeyError:
                print("Элемента ", product, " нет ассортименте")

        self.all_price()

    @staticmethod
    def menu():#print_menu
        for key in Order_item.list_product:
            print(key + ". " + Order_item.list_product[key].get_name() + " " + str(
                Order_item.list_product[key].get_price()))

    def products(self):
        print("_" * 60)
        Order.products(self) #print_products and super()

    def reset(self):#update

        print("Введите название новой позиции:")
        name = input()

        print("Введите цену: ")
        price = input()

        print("Введите артикул: ")
        art = input()

        Order_item.list_product[str(len(Order_item.list_product) + 1)] = Item(name, price, art, 1) #just apend
