import threading
import time

class Counter:
    def __init__(self):
        self.value = 0

    def inc(self, count):
        for i in range(count):
            self.value += 1

    def dec(self, count):
        for i in range(count):
            self.value -= 1

if __name__ == "__main__":
    c = Counter()
    t1 = threading.Thread(target=c.inc, args=(100_000,))
    t2 = threading.Thread(target=c.dec, args=(100_000,))
    [t.start() for t in (t1, t2)]
    [t.join() for t in (t1, t2)]

    print(f"Value: {c.value}")

