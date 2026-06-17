def create_file(name):
    with open(name, mode='w') as f:
        for _ in range(1_000):
            f.write('hello sync\n')
        print(f"File {name} is ready")


def main():
    create_file('one.txt')
    create_file('two.txt')
    create_file('three.txt')


main()
