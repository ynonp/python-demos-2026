import threading

class Counter:
    def __init__(self, start = 0):
        self.count = start
        
    def start(self):
        for i in range(1_000_000):
            self.count += 1
            self.count -= 1

if __name__ == "__main__":
    c = Counter()
    t1 = threading.Thread(target=c.start)
    t2 = threading.Thread(target=c.start)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Count = {c.count}")
