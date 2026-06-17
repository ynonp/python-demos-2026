import threading
import time


def is_prime(n):
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


def count_primes_in_range(start, end, results, index):
    """Count primes in [start, end) and store the result at results[index]."""
    count = 0
    for n in range(start, end):
        if is_prime(n):
            count += 1
    results[index] = count


def count_primes(limit, num_threads):
    """Count primes in [0, limit) using num_threads threads."""
    results = [0] * num_threads
    threads = []

    chunk = limit // num_threads
    for i in range(num_threads):
        start = i * chunk
        # last thread takes whatever is left over
        end = limit if i == num_threads - 1 else start + chunk
        t = threading.Thread(
            target=count_primes_in_range,
            args=(start, end, results, i),
        )
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return sum(results)


def main(num_threads=1):
    limit = 1_000_000
    start = time.perf_counter()
    total = count_primes(limit, num_threads)
    elapsed = time.perf_counter() - start
    print(f"{num_threads} thread(s): {total} primes below {limit} — {elapsed:.4f}s")
    return total


def sieve_of_eratosthenes(limit):
    """Classic Sieve of Eratosthenes — returns count of primes < limit."""
    if limit < 2:
        return 0
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False
    return sum(is_prime)


def main_sieve(limit=1_000_000):
    start = time.perf_counter()
    total = sieve_of_eratosthenes(limit)
    elapsed = time.perf_counter() - start
    print(f"Sieve of Eratosthenes: {total} primes below {limit} — {elapsed:.4f}s")
    return total


if __name__ == "__main__":
    results = []
    for n in (1, 2, 4):
        results.append(main(n))

    print()
    sieve_result = main_sieve()
    results.append(sieve_result)

    print()
    if len(set(results)) == 1:
        print(f"All runs returned the same result: {results[0]}")
    else:
        print(f"Runs returned DIFFERENT results: {results}")
