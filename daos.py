from sqlite3 import Connection
from dtos import *


class Suppliers:
    def __init__(self, conn: Connection):
        self._conn = conn
        self.__init_table__()

    def __init_table__(self):
        self._conn.execute("""CREATE TABLE suppliers(
        id INTEGER PRIMARY KEY,
        name STRING NOT NULL
        )""")

    def insert(self, supplier: Supplier):
        self._conn.execute("INSERT INTO suppliers(id, name) VALUES(?, ?)", (supplier.iD, supplier.name))


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
        # This method retrieves a Hat with the given topping.
        # If multiple hats provide this topping - it'll choose the one with the minimum supplier.id.
        # It returns a tuple (Hat, Supplier) of the retrieved hat, and it's supplier
        # If no suitable hat was found, the method returns (None, None)
        self._cur.execute("""SELECT hats.id, hats.topping, hats.supplier, hats.quantity, suppliers.name
        FROM hats
        INNER JOIN suppliers
        ON hats.supplier = suppliers.id
        WHERE hats.topping = ?
        ORDER BY suppliers.id
        LIMIT 1""", (topping,))

        result = self._cur.fetchone()
        if result is None:
            return None, None
        hat = Hat(result[0], result[1], result[2], result[3])
        supplier = Supplier(result[2], result[4])

        return hat, supplier

    def insert(self, hat: Hat):
        self._conn.execute("INSERT INTO hats(id, topping, supplier, quantity) VALUES(?, ?, ?, ?)",
                           (hat.iD, hat.topping, hat.supplier, hat.quantity))

    def update(self, hat: Hat):
        self._conn.execute("UPDATE hats SET topping = ?, supplier = ?, quantity = ? WHERE id = ?",
                           (hat.topping, hat.supplier, hat.quantity, hat.iD))


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

    def insert(self, order: Order):
        self._conn.execute("INSERT INTO orders(location, hat) VALUES(?, ?)", (order.location, order.hat))
