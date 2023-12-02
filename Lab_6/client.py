import socket
import json
from serialization import *
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect(('127.0.0.1', 50007))
#     s.sendall(b'Hello')
#     data = s.recv(102)
#
# print("Resv", repr(data))

def imail_input():
    email = input("Enter recipient email\n")
    message = input("Enter recipient message\n")

    return {
        "email": email,
        "message": message
    }

def try_send(data):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 50007))
        s.sendall(serialize(data))

        return s.recv(1024)

def do_work():
    while True:
        data = imail_input()
        response = try_send(data)
        print(response)
        response = deserialize(response)
        if response['isSuccess']:
            print("Success, to send more emails, press ant key")
            input()
        else:
            print(f"Error while processing email, try again\nError message: {response['message']}")
            continue

do_work()
