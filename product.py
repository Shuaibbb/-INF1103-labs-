
from abc import ABC, abstractmethod
from supplier import Supplier


class CanBeShipped(ABC):
    @abstractmethod
    def get_shipping_info(self) -> str:
        pass


class Product(ABC):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        supplier: Supplier
    ) -> None:
        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        if stock_quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")

        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock_quantity
        self.__supplier = supplier

    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    @property
    def supplier(self) -> Supplier:
        return self.__supplier

    def update_stock(self, new_stock: int) -> None:
        if new_stock < 0:
            raise ValueError("Stock quantity cannot be negative.")

        self.__stock = new_stock

    def display_information(self) -> None:
        print("Product ID:", self.__product_id)
        print("Name:", self.__name)
        print("Price: $", format(self.__price, ".2f"), sep="")
        print("Stock:", self.__stock)
        print("Supplier:", self.__supplier.name)

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass


class PhysicalProduct(Product):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        weight: float,
        supplier: Supplier
    ) -> None:
        super().__init__(
            product_id, name, price, stock_quantity, supplier
        )
        self.__weight = weight

    @property
    def weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print("Type: Physical Product")
        print("Weight:", self.__weight, "kg")

    def get_shipping_info(self) -> str:
        return f"Shipping weight: {self.__weight} kg"

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping."


class DigitalProduct(Product):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        download_size: float,
        supplier: Supplier
    ) -> None:
        super().__init__(
            product_id, name, price, stock_quantity, supplier
        )
        self.__download_size = download_size

    @property
    def download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print("Type: Digital Product")
        print("Download Size:", self.__download_size, "MB")

    def get_fulfilment_info(self) -> str:
        return "Delivered digitally."


CanBeShipped.register(PhysicalProduct)
