from datetime import datetime
from datetime import timedelta

from order import Order
from order_food import Order_food
from order_item import Order_item
from item import Item
import pickle

mas_order = []

try:
    with open("mas_order.bin", "rb") as f:
        mas_order = pickle.load(f)
        print("=" * 60)
        print("История заказов прочитана.")
        print("=" * 60 + "\n\n")
except FileNotFoundError:
    print("=" * 60)
    print("База данных пуста.")
    print("=" * 60 + "\n\n")
except EOFError as e:
    pass

try:
    with open("list_product_food.bin", "rb") as f:
        Order_food.list_product = pickle.load(f)
        print("=" * 60)
        print("Меню прочитано.")
        print("=" * 60 + "\n\n")
except FileNotFoundError:
    print("=" * 60)
    print("Установлено меню по умолчанию")
    print("=" * 60 + "\n\n")
except EOFError as e:
    pass

try:
    with open("list_product_item.bin", "rb") as f:
        Order_item.list_product = pickle.load(f)
        print("=" * 60)
        print("Ассортимент прочитан.")
        print("=" * 60 + "\n\n")
except FileNotFoundError:
    print("=" * 60)
    print("Установлен ассортимент по умолчанию")
    print("=" * 60 + "\n\n")
except EOFError as e:
    pass

while True:
    print("=" * 60)
    value = input("\nМеню:\n\t0 - Просмотреть меню и ассортимент\n\t1 - Cоздать новый заказ \n\t2 - Вывести список заказов\n\t3 - Сравнить содержимое двух заказов\n\t4 - Вывести подробную информацию"
                  "о заказе\n\t5 - Удалить позицию из заказа\n\t6 - Сообщить о доставке\n\t7 - Просмотреть данные о состоянии\n\t8 - Отредактировать "
                  "данные в меню (только для Admin)\n\t9 - Отредактировать позицию в меню (только для Admin)\n\t10 - Завершить работу\n")
    print("=" * 60)
    match value:
        case "0":
            print("\nПродуктовый заказ")
            Order_food.menu()
            print("\nОбычный заказ")
            Order_item.menu()
        case "1":
            value = input("Продуктовый заказ - 1, обычный заказ - 2: ")
            match value:
                case "1":
                    mas_order.append(Order_food())
                case "2":
                    mas_order.append(Order_item())
                case _:
                    print("Что это было?")
        case "2":
            m_2 = 1
            for element in mas_order:
                print(str(m_2) + str(element))
                m_2 += 1
        case "3":
            line = input("\nВведите через пробел порядковые номера двух заказов: ")
            try:
                if (mas_order[int(line.split()[0]) - 1].equals(mas_order[int(line.split()[1]) - 1])):
                    print("Состав этих заказов абсолютно идентичен")
                else:
                    print("Некотрые позиции отличаются")
            except ValueError as e:
                print("\nВведены некорректные значения!\n")
                print(e)
            except IndexError as e:
                print("\nУказан некорректный номер заказа. Сверьтесь со список по команде №2\n")
                print(e)
            except Exception as e:
                print("\nОшибка. Попробуйте ещё раз\n")
                print(e)
        case "4":
            try:
                value = int(input("\nВведите порядковый номер заказа: "))
                print("=" * 60)
                if type(mas_order[value - 1]) == Order_food:
                    print("ЗАКАЗ №" + str(value) + " (Продуктовый)")
                else:
                    print("ЗАКАЗ №" + str(value) + " (Обычный)")
                mas_order[value - 1].products()
                print("=" * 60)
            except ValueError as e:
                print("\nВведены некорректные значения!\n")
                print(e)
            except IndexError as e:
                print("\nУказан некорректный номер товара\n")
                print(e)
            except Exception as e:
                print("\nОшибка. Попробуйте ещё раз\n")
                print(e)
        case "5":
            value = int(input("Введите номер заказа, который вы хотите изменить: "))
            line = input("Введите наименование позиции, которую вы хотите удалить из заказа: ")

            try:
                mas_order[value - 1] - line
            except ValueError as e:
                print("\nВведены некорректные значения!\n")
                print(e)
            except IndexError as e:
                print("\nУказан некорректный номер заказа\n")
                print(e)
            except Exception as e:
                print("\nОшибка. Попробуйте ещё раз\n")
                print(e)

        case "6":
            value = int(input("Введите номер заказа, который вы хотите изменить: "))
            try:
                mas_order[value - 1].accept()
            except IndexError as e:
                print("\nУказан некорректный номер заказа\n")
                print(e)
        case "7":
            value = int(input("Введите номер заказа, статус которого Вас интересует: "))
            try:
                mas_order[value - 1].delivery()
            except IndexError as e:
                print("\nУказан некорректный номер заказа\n")
                print(e)
        case "8":
            print("Введите номер раздела, позицию в котором вы хотите добавить позицию.")
            value = input("Продуктовый заказ - 1, обычный заказ - 2: ")
            match value:
                case "1":
                    Order_food.reset()
                case "2":
                    Order_item.reset()
                case _:
                    print("Что это было?")
        case "9":
            print("Введите номер раздела, позицию в котором вы хотите добавить позицию.")
            value = input("Продуктовый заказ - 1, обычный заказ - 2: ")
            match value:
                case "1":
                    Order_food.menu()
                    print("Введите порядковый номер позиции, которую вы хотите отредактривать: ")
                    value = input()
                    try:
                        Order_food.list_product[str(value)].set_name(input("Введите название товара: "))
                        Order_food.list_product[str(value)].set_price(input("Введите стоимость товара: "))
                        Order_food.list_product[str(value)].set_art(input("Введите артикул товара: "))
                    except ValueError as e:
                        print("\nВведены некорректные значения!\n")
                        print(e)
                    except IndexError as e:
                        print("\nУказан некорректный номер заказа\n")
                        print(e)
                    except Exception as e:
                        print("\nОшибка. Попробуйте ещё раз\n")
                        print(e)

                case "2":
                    Order_item.menu()
                    print("Введите порядковый номер позиции, которую вы хотите отредактривать: ")
                    value = input()
                    try:
                        Order_item.list_product[str(value)].set_name(input("Введите название товара: "))
                        Order_item.list_product[str(value)].set_price(input("Введите стоимость товара: "))
                        Order_item.list_product[str(value)].set_art(input("Введите артикул товара: "))
                    except ValueError as e:
                        print("\nВведены некорректные значения!\n")
                        print(e)
                    except IndexError as e:
                        print("\nУказан некорректный номер заказа\n")
                        print(e)
                    except Exception as e:
                        print("\nОшибка. Попробуйте ещё раз\n")
                        print(e)
                case _:
                    print("Что это было?")
        case "10":
            try:
                with open("mas_order.bin", "wb") as f:
                    pickle.dump(mas_order, f)
                    print("=" * 60)
                    print("База данных успешно сохранена!")
                    print("=" * 60)
            except Exception as e:
                print("Не удалось сохранить данные")
                print(e)

            try:
                with open("list_product_food.bin", "wb") as f:
                    pickle.dump(Order_food.list_product, f)
                    print("=" * 60)
                    print("Меню успешно сохранено!")
                    print("=" * 60)
            except Exception as e:
                print("Не удалось сохранить данные")
                print(e)

            try:
                with open("list_product_item.bin", "wb") as f:
                    pickle.dump(Order_item.list_product, f)
                    print("=" * 60)
                    print("Ассортимент успешно сохранен!")
                    print("=" * 60)
            except Exception as e:
                print("Не удалось сохранить данные")
                print(e)

            print(mas_order[0].price)
            break
        case _:
            print("Что это было?")