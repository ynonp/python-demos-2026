from multiprocessing import Pool
from math import sqrt
import time

def isprime(n: int):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    p = Pool(5)
    start = time.perf_counter()
    print(sum(p.map(isprime, range(2, 1_000_000))))

    p.close()
    elapsed = time.perf_counter() - start
    print(f"{elapsed:.4f}s")














