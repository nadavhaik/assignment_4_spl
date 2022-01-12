class Supplier:
    def __init__(self, iD: int, name: str):
        self.iD = iD
        self.name = name


class Hat:
    def __init__(self, iD: int, topping: str, supplier: int, quantity: int):
        self.iD = iD
        self.topping = topping
        self.supplier = supplier
        self.quantity = quantity


class Order:
    def __init__(self, location: str, hat: int, iD: int = None):    # The id is calculated in DB -
                                                                    # isn't necessary for inserts.
        self.location = location
        self.hat = hat
        self.iD = iD
