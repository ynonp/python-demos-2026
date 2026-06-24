class Database:
    def __init__(self):
        print("Initializing database...")
        self.connected = False

db1 = Database()
db2 = Database()
db1.connected = True
print(db2.connected)

