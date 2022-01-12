from sqlite3 import Connection


class Suppliers:
    def __init__(self, conn: Connection):
        self._conn = conn
        self.__init_table__()

    def __init_table__(self):
        self._conn.execute("""CREATE TABLE suppliers(
        id INTEGER PRIMARY KEY,
        name STRING NOT NULL
        )""")

    def insert(self, iD: int, name: str):
        self._conn.execute("INSERT INTO suppliers(id, name) VALUES(?, ?)", (iD, name))


class Hats:
    def __init__(self, conn: Connection):
        self._conn = conn
        self._cur = conn.cursor()
        self.__init_table__()

    def __init_table__(self):
        self._conn.execute("""CREATE TABLE hats(
        id INTEGER PRIMARY KEY,
        topping STRING NOT NULL,
        supplier INTEGER REFERENCES suppliers(id),
        quantity INTEGER NOT NULL
        )""")

        # This trigger is responsible for deleting a hat when it's quantity drops to zero
        self._conn.execute("""CREATE TRIGGER hats_delete_zero_quantity
        AFTER UPDATE OF quantity ON hats
        FOR EACH ROW
        WHEN NEW.quantity=0
        BEGIN 
            DELETE FROM hats WHERE id = NEW.id;
        END;
        """)

    def get_next_by_topping(self, topping: int):
        # This method retrieves a hat with the given topping.
        # If multiple hats provide this topping - it'll choose the one with the minimum supplier.id.
        # The method returns a tuple(int, str): the id of the chosen hat, and the name of the supplier linked to it.
        # If no suitable hat was found, the method returns both values None.
        self._cur.execute("""SELECT hats.id, suppliers.name
        FROM hats
        INNER JOIN suppliers
        ON hats.supplier = suppliers.id
        WHERE hats.topping = ?
        ORDER BY suppliers.id
        LIMIT 1""", (topping,))

        result = self._cur.fetchone()
        if result is None:
            return None, None
        return result

    def insert(self, iD: int, topping: str, supplier: int, quantity: int):
        self._conn.execute("INSERT INTO hats(id, topping, supplier, quantity) VALUES(?, ?, ?, ?)",
                           (iD, topping, supplier, quantity))

    def decrement_quantity(self, iD: int):
        self._conn.execute("UPDATE hats SET quantity = quantity-1 WHERE id = ?", (iD,))


class Orders:
    def __init__(self, conn: Connection):
        self._conn = conn
        self.__init_table__()

    def __init_table__(self):
        self._conn.execute("""CREATE TABLE orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location STRING NOT NULL,
        hat INTEGER REFERENCES hats(id)
        )""")

    def insert(self, location: str, hat_id: int):
        self._conn.execute("INSERT INTO orders(location, hat) VALUES(?, ?)", (location, hat_id))
