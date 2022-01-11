import sqlite3
import os


class ContextManager:
    def __init__(self, config_file_path: str, orders_file_path: str, output_file_path: str, output_db_path: str):
        self.config_file_path = config_file_path
        self.orders_file_path = orders_file_path
        self.output_file_path = output_file_path
        self.output = ""
        if os.path.isfile(output_db_path):
            # Deleting the old db if exists
            os.remove(output_db_path)
        self.conn = sqlite3.connect(output_db_path)
        self.cur = self.conn.cursor()

    def write_output_file(self):
        with open(self.output_file_path, 'w') as output_file:
            output_file.write(self.output)

    def build_schema(self):
        self.conn.execute("""CREATE TABLE suppliers(
        id INTEGER PRIMARY KEY,
        name STRING NOT NULL
        )""")

        self.conn.execute("""CREATE TABLE hats(
        id INTEGER PRIMARY KEY,
        topping STRING NOT NULL,
        supplier INTEGER REFERENCES suppliers(id),
        quantity INTEGER NOT NULL
        )""")

        self.conn.execute("""CREATE TABLE orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location STRING NOT NULL,
        hat INTEGER REFERENCES hats(id)
        )""")

        self.conn.execute("""CREATE TRIGGER delete_empty_hats
        AFTER UPDATE OF quantity ON hats
        FOR EACH ROW
        WHEN NEW.quantity=0
        BEGIN 
            DELETE FROM hats WHERE id = NEW.id;
        END;
        """)

        self.conn.commit()

    def init_db(self):
        with open(self.config_file_path, 'r') as file:
            config_lines = file.read().splitlines()

        line_numbers = config_lines[0].split(sep=",")
        number_of_hats = int(line_numbers[0])
        number_of_suppliers = int(line_numbers[1])

        # Creating suppliers before hats:
        for i in range(number_of_hats + 1, number_of_hats + number_of_suppliers + 1):
            supplier_data = config_lines[i].split(sep=",")
            self.conn.execute("INSERT INTO suppliers(id, name) VALUES(?, ?)", supplier_data)

        for i in range(1, number_of_hats + 1):
            hat_data = config_lines[i].split(sep=",")
            self.conn.execute("INSERT INTO hats(id, topping, supplier, quantity) VALUES(?, ?, ?, ?)", hat_data)

        self.conn.commit()

    def execute_orders(self):
        with open(self.orders_file_path) as file:
            order_lines = file.read().splitlines()

        line_num = 1
        for order_line in order_lines:
            location, topping = order_line.split(",")
            self.cur.execute("""SELECT hats.id, suppliers.id, suppliers.name
            FROM hats
            INNER JOIN suppliers
            ON hats.supplier = suppliers.id
            WHERE hats.topping = ?
            ORDER BY suppliers.id
            LIMIT 1""", (topping,))
            result = self.cur.fetchone()

            if result is None:
                raise ValueError(f"Illegal input - no hat was found for order {location},{topping} in line: {line_num}.")
            hat_id, supplier_id, supplier_name = result

            self.conn.execute("INSERT INTO orders(location, hat) VALUES(?, ?)", (location, hat_id))

            self.conn.execute("UPDATE hats SET quantity = quantity-1 WHERE id = ?", (hat_id,))

            self.conn.commit()
            self.output += f"{topping},{supplier_name},{location}\n"
            line_num += 1

    def run(self):
        self.build_schema()
        self.init_db()
        self.execute_orders()
        self.write_output_file()
        self.conn.close()
