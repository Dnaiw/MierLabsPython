import os


def validate_input(string_input):
    for letter in string_input:
        if  (ord(letter) >= ord("0") or ord(letter) <= ord("9")):
            return True
        if ord(letter) >= ord("A") or ord(letter) <= ord("z"):
            return True

    return False

def find_files_by_substring(dir, substring):
    all_files = os.listdir(dir)
    found_files = [x for x in all_files if substring in x]
    return len(found_files)


while True:
    substring = input("Type a string, which contains latin letters and digits\n")

    if not(validate_input(substring)):
        print("Error: invalid input")
        continue

    result = find_files_by_substring("example", substring)
    print(result)
    break

