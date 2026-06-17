import threading
import time
from random import randint

class Producer:
    def __init__(self):
        self.count = 10
        self.data = []
        self.condition = threading.Condition()

    def flusher(self):
        while True:
            with self.condition:
                self.condition.wait_for(lambda: len(self.data) >= 10)

                batch = self.data
                self.data = []

            print(f"Flushing batch of {len(batch)}: {batch}")

    def run(self):
        while self.count > 0:
            with self.condition:
                self.data.append(randint(0, 100))

                if len(self.data) >= 10:
                    self.condition.notify()

            time.sleep(0.1)
            self.count -= 1


if __name__ == "__main__":
    p = Producer()

    t = threading.Thread(target=p.flusher, daemon=True)
    t.start()

    p.run()
    print("=== The End ===")

