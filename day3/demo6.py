import multiprocessing
import time

def say_hello(process_name):
    for i in range(10):
        print(f"Hello {process_name}. i = {i}")
        time.sleep(0.1)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=say_hello, args=("process 1",))
    p2 = multiprocessing.Process(target=say_hello, args=("process 2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


