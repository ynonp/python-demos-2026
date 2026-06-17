import threading
from concurrent.futures import ThreadPoolExecutor
import time

def say_hi(name: str):
    for i in range(10):
        print(f"Hello {name}; i = {i}; thread = {threading.current_thread()}")
        time.sleep(0.1)
    return len(name)

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as p:
        f1 = p.submit(say_hi, "process 1")
        f2 = p.submit(say_hi, "process 2")
        p.submit(say_hi, "process 3")
        p.submit(say_hi, "process 4")
        p.submit(say_hi, "process 5")
        p.submit(say_hi, "process 6")

        print("==== 1 ")
        print(type(f1))
        print(type(f2))
        print("==== 2 ")
        print(f1.result())
        print(f2.result())
