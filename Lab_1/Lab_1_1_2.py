def validate_input(input_string):
    for letter in input_string:
        if ord(letter) < ord("A") or ord(letter) > ord("z"):
            return False
    return True


def palindrom(word):
    length = len(word)
    word = word.lower()

    if length % 2 == 0 and word[:length // 2] == word[length // 2:][::-1]:
        return True

    if length % 2 == 1 and word[:length // 2] == word[length // 2 + 1:][::-1]:
        return True

    return False


def task(word):
    result = 0

    if palindrom(word[1:]):
        result += 1

    for i in range(1, len(word)):
        new_word = (word[:i - 1] + word[i:])

        if palindrom(new_word):
            result += 1

    return result


while True:
    word = input("Please, type a word, only latin letters are available\n")

    if not (validate_input(word)):
        print("Error: invalid input")
        continue

    print(f"Result: {task(word)}")
    break
