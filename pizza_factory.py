from dtos import *
from repository import Repository


class PizzaFactory:
    def __init__(self, config_file_path: str, orders_file_path: str, output_file_path: str, output_db_path: str):
        self.config_file_path = config_file_path
        self.orders_file_path = orders_file_path
        self.output_file_path = output_file_path
        self.output = ""
        self.rep = Repository(output_db_path)

    def write_output_file(self):
        with open(self.output_file_path, 'w') as output_file:
            output_file.write(self.output)

    def populate_db(self):
        with open(self.config_file_path, 'r') as file:
            config_lines = file.read().splitlines()

        line_numbers = config_lines[0].split(sep=",")
        number_of_hats = int(line_numbers[0])
        number_of_suppliers = int(line_numbers[1])

        # Creating suppliers before hats:
        for i in range(number_of_hats + 1, number_of_hats + number_of_suppliers + 1):
            iD, name = config_lines[i].split(sep=",")
            self.rep.suppliers.insert(Supplier(iD, name))

        for i in range(1, number_of_hats + 1):
            iD, topping, supplier, quantity = config_lines[i].split(sep=",")
            self.rep.hats.insert(Hat(iD, topping, supplier, quantity))

        self.rep.commit()

    def execute_orders(self):
        with open(self.orders_file_path) as file:
            order_lines = file.read().splitlines()

        line_num = 1
        for order_line in order_lines:
            location, topping = order_line.split(",")
            hat, supplier = self.rep.hats.get_next_by_topping(topping)
            if hat is None:
                raise ValueError("Illegal input - no hat was found for order "
                                 +f"{location},{topping} in line: {line_num}.")

            hat.quantity-=1
            self.rep.orders.insert(Order(location, hat.iD))
            self.rep.hats.update(hat)  # When the quantity drops to 0 - a special trigger deletes it.
            self.rep.commit()

            self.output += f"{topping},{supplier.name},{location}\n"
            line_num += 1

    def feed_hungry_people(self):
        self.populate_db()
        self.execute_orders()
        self.write_output_file()
        self.rep.close()
