def count_primes(n):
    if n < 2:
        return 0
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i:n:i] = [False] * len(range(i*i, n, i))
    return sum(sieve)

if __name__ == "__main__":
    prime_count = count_primes(100_000)
    print(prime_count)
