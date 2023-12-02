import email
import imaplib
import time
from os import getenv
from dotenv import load_dotenv, find_dotenv


def read_email_from_gmail(count=10, contain_body=False):

    mail = imaplib.IMAP4_SSL(getenv("IMAP_HOST"), int(getenv("IMAP_PORT")))
    mail.login(getenv("EMAIL_LOGIN"), getenv("EMAIL_PASSWORD"))

    res, messages = mail.select('INBOX')

    messages = int(messages[0])

    # Iterating over the sent emails
    for i in range(messages, messages - count, -1):
        # RFC822 protocol
        res, msg = mail.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])

                sender = msg["From"]
                subject = msg["Subject"]

                if not("Mailer" in str(subject)):
                    continue

                body = ""
                temp = msg
                if temp.is_multipart():
                    for part in temp.walk():
                        ctype = part.get_content_type()
                        cdispo = str(part.get('Content-Disposition'))

                        # skip text/plain type
                        if ctype == 'text/plain' and 'attachment' not in cdispo:
                            body = part.get_payload(decode=True)  # decode
                            break
                else:
                    body = temp.get_payload(decode=True)

                # Print Sender, Subject, Body
                print("-"*50)  # To divide the messages
                print("From    : ", sender)
                print("Subject : ", subject)
                if(contain_body):
                    print("Body    : ", body.decode())

    mail.close()
    mail.logout()

def do_work():
    load_dotenv(find_dotenv())

    while True:
        read_email_from_gmail()
        time.sleep(float(getenv("PERIOD_CHECK")))


do_work()
