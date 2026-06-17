import timeit
import re

def is_id_invalid_1(id: str):
    return id[0:len(id) // 2] == id[len(id) // 2:len(id)]

def is_id_invalid_2(id: str):
    return re.search(r"^(.+)\1$", id) is not None

if __name__ == "__main__":
    for id in ["11", "123123", "9191", "100100", "910910", "1234", "123123123"]:
        assert is_id_invalid_1(id) == is_id_invalid_2(id), id

    print(timeit.timeit(lambda: is_id_invalid_1("123123"), number=1000))
    print(timeit.timeit(lambda: is_id_invalid_2("123123"), number=1000))

    print(timeit.timeit(lambda: is_id_invalid_1("1231231231231231231"), number=1000))
    print(timeit.timeit(lambda: is_id_invalid_2("1231231231231231231"), number=1000))

