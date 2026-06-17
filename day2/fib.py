import tracemalloc
import itertools
import sys

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

sys.set_int_max_str_digits(999999999)
if __name__ == "__main__":
    tracemalloc.start()
    snap1 = tracemalloc.take_snapshot()
    print(sum(itertools.islice(fib(), 100_000)))

    snap2 = tracemalloc.take_snapshot()
    stats = snap2.compare_to(snap1, 'lineno')

    for stat in stats[:50]:
        print(stat)

    total_objects_diff = sum(stat.count_diff for stat in stats)

    # x = next(itertools.islice(fib(), 8, None))
    # print(x)
