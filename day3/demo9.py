from concurrent.futures import ThreadPoolExecutor
import threading
import time
def is_prime(n):
    # print(f"{threading.current_thread()} Checking: {n}")
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as p:
        start = time.perf_counter()
        results = p.map(is_prime, range(1_000_000), chunksize=50_000)

        print(sum(results))
        elapsed = time.perf_counter() - start
        print(f"{elapsed:.4f}s")
