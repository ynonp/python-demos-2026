class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        print(f"New {cls} is created")
        return super().__call__(*args, **kwargs)

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Initializing database...")
        self.connected = True

x = Database()
