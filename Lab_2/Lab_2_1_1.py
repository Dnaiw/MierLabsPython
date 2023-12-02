import random


def generate_ip():
    return f"{random.randint(0,256)}.{random.randint(0,256)}.{random.randint(0,256)}.{random.randint(0,256)}"

def get_unique_ips_list():
    result = []
    while(len(result) < 1000):
        ip = generate_ip()
        if not(ip in result):
            result.append(ip)

    return result

with open("ip.log", "w") as file:
    ips = get_unique_ips_list()
    for ip in ips:
        file.write(ip)
        file.write("\n")

