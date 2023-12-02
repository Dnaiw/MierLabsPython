from functools import cmp_to_key


def validate_input(string_input):
    for letter in string_input:
        if letter != " " and (ord(letter) < ord("1") or ord(letter) > ord("9")):
            return False

    return True


def get_bin_sum(number):
    string_num = str(bin(number))[2:]
    return sum([int(x) for x in string_num])


def compare(item1, item2):
    if get_bin_sum(item1) < get_bin_sum(item2):
        return -1
    if get_bin_sum(item1) > get_bin_sum(item2):
        return 1
    if item1 < item2:
        return -1
    if item1 > item2:
        return 1
    return 0


while True:
    string_input = input("Please, type numbers divided by space\n")

    if not (validate_input(string_input)):
        print("Error: invalid input")
        continue

    int_list = [int(x) for x in string_input.split(" ")]
    int_list.sort(key=cmp_to_key(compare))

    print(f"Result: {int_list}")
    break
