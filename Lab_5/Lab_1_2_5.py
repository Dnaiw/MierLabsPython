from threading import Thread
from queue import Queue


def fillQeueu(q):
    for i in range(50):
        q.put(
            {
                "url": f"some url {i}",
                "bigData": f"Very big data {i}"
            }
        )
    q.put(None)
    q.put(None)

def worker(q, n):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"\nThread_{n} - Process data: {item['bigData']} from url: {item['url']}")

q = Queue()
fillQeueu(q)
th1 = Thread(target=worker, args=(q,1))
th2 = Thread(target=worker, args=(q,2))
th1.start()
th2.start()



