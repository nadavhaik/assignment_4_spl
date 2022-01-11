from database import DataBase


class ContextManager:
    def __init__(self, config_file_path: str, orders_file_path: str, output_file_path: str, output_db_path: str):
        self.config_file_path = config_file_path
        self.orders_file_path = orders_file_path
        self.output_file_path = output_file_path
        self.output = ""
        self.db = DataBase(output_db_path)

    def write_output_file(self):
        with open(self.output_file_path, 'w') as output_file:
            output_file.write(self.output)

    def init_db(self):
        with open(self.config_file_path, 'r') as file:
            config_lines = file.read().splitlines()

        line_numbers = config_lines[0].split(sep=",")
        number_of_hats = int(line_numbers[0])
        number_of_suppliers = int(line_numbers[1])

        # Creating suppliers before hats:
        for i in range(number_of_hats + 1, number_of_hats + number_of_suppliers + 1):
            iD, name = config_lines[i].split(sep=",")
            self.db.suppliers.insert(iD, name)

        for i in range(1, number_of_hats + 1):
            iD, topping, supplier, quantity = config_lines[i].split(sep=",")
            self.db.hats.insert(iD, topping, supplier, quantity)

        self.db.commit()

    def execute_orders(self):
        with open(self.orders_file_path) as file:
            order_lines = file.read().splitlines()

        line_num = 1
        for order_line in order_lines:
            location, topping = order_line.split(",")
            result = self.db.hats.get_next_by_topping(topping)
            if result is None:
                raise ValueError(
                    f"Illegal input - no hat was found for order {location},{topping} in line: {line_num}.")
            hat_id, supplier_name = result

            self.db.orders.insert(location, hat_id)
            self.db.hats.decrement_quantity(hat_id)  # When the quantity drops to 0 - a special trigger deletes it.
            self.db.commit()
            self.output += f"{topping},{supplier_name},{location}\n"
            line_num += 1

    def run(self):
        self.init_db()
        self.execute_orders()
        self.write_output_file()
