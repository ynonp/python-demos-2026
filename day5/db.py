class Database:
    _shared_state = { "connected": False }

    def __init__(self):
        print("Initializing database...")
        self.__dict__ = self._shared_state
        if not self.connected:
            print("Connecting")
            self.connected = True

db1 = Database()
db2 = Database()
print(Database._shared_state)

db1.connected = False
print(db2.connected)