import re
import socket
import random
from smtplib import SMTP
import json
from serialization import *
from os import getenv
from dotenv import load_dotenv, find_dotenv


def generate_random_id():
    # Generate a random 5-digit ID
    random_id = ''.join(random.choice('0123456789') for _ in range(5))
    return random_id

def start_listening():
    load_dotenv(find_dotenv())

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 50007))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            while True:
                raw_data = conn.recv(1024)
                if not(raw_data):
                    continue

                data = deserialize(raw_data)

                isSuccess, message = validate_data(data)

                response_data ={
                    "isSuccess": isSuccess,
                    "message": message
                }
                conn.sendall(serialize(response_data))

                if not(isSuccess):
                    print("error")
                    continue

                send_email(data['email'], data['message'])

def validate_data(data):
    print("begin validation")
    if not('email' in data):
        return False, "Email not found in data"
    if not('message' in data):
        return False, "Message not found in data"

    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")

    if not re.match(pattern, data['email']):
        return False, "Invalid email"
    if len(data['message']) < 1:
        return False, "Empty message"

    print("finish validation")
    return True, "validation passed"

def send_email(email, message):
    print("sending email")
    with SMTP(f"{getenv('SMTP_HOST')}:{int(getenv('SMTP_PORT'))}") as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("dnk160604@gmail.com", "fkuy cgzr aqdl ucnf")
        smtp.sendmail(
            "dnk160604@gmail.com",
            email,
            f"Subject:[Ticket #{generate_random_id()}]Mailer\n{message}"
        )
        smtp.sendmail(
            "dnk160604@gmail.com",
            "dnk160604@gmail.com",
            f"Ticket #{generate_random_id()}]Mailer\nEmail with text <{message}> sent to {email}"
        )


start_listening()