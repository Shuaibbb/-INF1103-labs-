
from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, new_stock):
        if new_stock < 0:
            raise ValueError("Stock cannot be negative.")
        self.stock = new_stock

    def display_information(self):
        print("ID:", self.product_id)
        print("Name:", self.name)
        print("Price: $" + format(self.price, ".2f"))
        print("Stock:", self.stock)

    @abstractmethod
    def get_fulfilment_info(self):
        pass


class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.weight = weight

    def display_information(self):
        super().display_information()
        print("Weight:", self.weight, "kg")

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        return 5 + self.weight * 2


CanBeShipped.register(PhysicalProduct)


class DigitalProduct(Product):
    def __init__(
        self, product_id, name, price, stock, download_size
    ):
        super().__init__(product_id, name, price, stock)
        self.download_size = download_size

    def display_information(self):
        super().display_information()
        print("Download Size:", self.download_size, "MB")

    def get_fulfilment_info(self):
        return "Delivered digitally."
