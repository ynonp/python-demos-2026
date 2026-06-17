import threading
import time

def print_hello(thread_name):
    for i in range(3):
        print(f"{thread_name}: {i}")
        time.sleep(0.5)


if __name__ == "__main__":
    t1 = threading.Thread(target=print_hello, args=("Thread 1",))
    t2 = threading.Thread(target=print_hello, args=("Thread 2",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("The End")
