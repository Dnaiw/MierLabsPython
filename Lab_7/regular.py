from regular_exeption import RegularExeption

def regular_line(line: str) -> str:
    line = str(line)
    try:
        for i in line.lower():
            if ord(i) not in range(ord('а'), ord('я') + 1) and ord(i) != ord('ё') and ord(i) != ord(" "):
                raise RegularExeption(1, line)
    except RegularExeption:
        return "Nothing"
    else:
        return line
#No sense in throwing errors
#Bad naming RegularExpression

def regular_digit(dig: str) -> int:
    dig = str(dig)
    try:
        if not dig.isdigit():
            raise RegularExeption(2, dig)
        if  int(dig) < 0:
            raise RegularExeption(2, dig)
    except RegularExeption:
        return 0
    else:
        return int(dig)
