from threading import Thread
from queue import Queue
import time

import requests

urls = [
    "https://yandex.ru",
    "https://vk.com",
    "https://mail.ru",
    "https://rambler.ru",
    "https://lenta.ru",
    "https://tass.ru",
    "https://ria.ru",
    "https://gazeta.ru",
    "https://rt.com",
"https://yandex.ru",
    "https://vk.com",
    "https://mail.ru",
    "https://rambler.ru",
    "https://lenta.ru",
    "https://tass.ru",
    "https://ria.ru",
    "https://gazeta.ru",
    "https://rt.com"
]

def get_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return r.text
    return r.text

def save_to_file(text, filename, filepath = r"D:\LABS\Python\Lab_5\web_pages"):
    with open(filepath + "\\" + filename + ".txt", "a", encoding='utf-8') as file:
        file.write(text)

def process_url_from_queue(q):
    while True:
        url = q.get()
        if url is None:
            break

        save_to_file(get_url(url), url[8:])

def process_concurrently():
    q = Queue()
    for url in urls :
        q.put(url)
    q.put(None)
    q.put(None)

    th1 = Thread(target=process_url_from_queue, args=(q,))
    th2 = Thread(target=process_url_from_queue, args=(q,))
    th1.start()
    th2.start()

def process_consistently():
    for url in urls:
        save_to_file(get_url(url), url[8:])

if __name__ == '__main__':
    start1 = time.time()
    process_consistently()
    end1 = time.time()
    start2 = time.time()
    process_concurrently()
    end2 = time.time()
    print(f"Consistently: {end1 - start1}")
    print(f"Concurrently: {end2 - start2}")