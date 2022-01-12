import sqlite3
import os
from tables import *


class Repository:
    def __init__(self, output_db_path: str):
        if os.path.isfile(output_db_path):
            # Deleting the old db if exists
            os.remove(output_db_path)
        self._conn = sqlite3.connect(output_db_path)
        self.suppliers = Suppliers(self._conn)
        self.hats = Hats(self._conn)
        self.orders = Orders(self._conn)
        self.commit()  # After creating tables and triggers

    def commit(self):
        self._conn.commit()

    def close(self):
        self._conn.close()
