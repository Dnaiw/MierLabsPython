def validate_ip(ip):
    if ip.count(".") != 3:
        return False

    parts = []
    try:
        parts = [int(x) for x in ip.split(".")]
    except:
        return False

    for part in parts:
        if part < 0 or part > 255:
            return False

    return True


def get_subnet_address(ip, mask):
    return ".".join(map(str, [i & m
          for i,m in zip(map(int, ip.split(".")),
                         map(int, mask.split(".")))]))

def get_ips_from_log(file_name):
    with open(file_name, "r") as file:
        result = file.read().split("\n")[:-1:]

    return result

while True:
    mask = input("Type a mask in format X.X.X.X\n")

    if not(validate_ip(mask)):
        print("Error: invalid mask format")

    break


ips = get_ips_from_log("ip.log")

with open("ip_solve.log", "w") as file:
    for ip in ips:
        file.write(get_subnet_address(ip, mask))
        file.write("\n")



