def get_text_from_file(file_path):
    result = ""
    with open(file_path, "r", encoding="utf-8") as file:
        result = file.read()
    return result

def get_letters_rate(text):
    result = {chr(letter): 0 for letter in range(ord('а'), ord('я') + 1)}
    result['ё'] = 0
    all_letters = 0
    for key in result:
        repeats = text.count(key) + text.count(key.upper())
        result[key] = repeats
        all_letters += repeats

    for key in result:
        result[key] /= all_letters

    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

def save_letters_rate_to_file(file_path, rate):
    with open(file_path, "w", encoding="utf-8") as file:
        for key in rate:
            file.write(f"{key}: {rate[key]}\n")


text = get_text_from_file("article_rus.txt")
rate = get_letters_rate(text)
save_letters_rate_to_file("article_rus_solve.txt", rate)


