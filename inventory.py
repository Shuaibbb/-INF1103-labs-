import json
import os
from product import Product, PhysicalProduct, DigitalProduct
from product_factory import ProductFactory
from supplier import Supplier


class Inventory:
    def __init__(self, filename: str = "inventory.json") -> None:
        self.products: list[Product] = []
        self.filename = filename
        self.load_inventory()

    def display_all(self) -> None:
        print("\nCurrent Inventory")
        print("----------------------------------------")

        if not self.products:
            print("Inventory is empty.")
        else:
            for product in self.products:
                print()
                product.display_information()

        print("----------------------------------------")

    def add_product(self, product: Product) -> None:
        if self.find_product(product.product_id) is not None:
            print("Product ID already exists.")
            return

        self.products.append(product)
        print("Product added successfully!")

    def remove_product(self, product_id: str) -> Product | None:
        product = self.find_product(product_id)

        if product is not None:
            self.products.remove(product)
            print("Product removed from inventory.")
            return product

        print("Product not found.")
        return None

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    # Keep this for compatibility with your Lab 7 menu
    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    def update_stock(self, product_id: str, new_stock: int) -> None:
        product = self.find_product(product_id)

        if product is not None:
            product.update_stock(new_stock)
            print("Stock updated successfully!")
        else:
            print("Product not found.")

    def save_inventory(self) -> None:
        data = []

        for product in self.products:
            item = {
                "id": product.product_id,
                "name": product.name,
                "price": product.price,
                "stock": product.stock,
                "supplier": {
                    "supplier_id": product.supplier.supplier_id,
                    "name": product.supplier.name,
                    "contact_email": product.supplier.contact_email
                }
            }

            if isinstance(product, PhysicalProduct):
                item["type"] = "physical"
                item["weight"] = product.weight

            elif isinstance(product, DigitalProduct):
                item["type"] = "digital"
                item["download_size"] = product.download_size

            data.append(item)

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Inventory saved successfully.")

    def load_inventory(self) -> None:
        if not os.path.exists(self.filename):
            print("Starting with an empty inventory.")
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            loaded_products: list[Product] = []
            suppliers: dict[str, Supplier] = {}

            for item in data:
                supplier_data = item.get("supplier", {
                    "supplier_id": "S000",
                    "name": "Unknown Supplier",
                    "contact_email": "unknown@example.com"
                })

                supplier_id = supplier_data["supplier_id"]

                if supplier_id not in suppliers:
                    suppliers[supplier_id] = Supplier(
                        supplier_id,
                        supplier_data["name"],
                        supplier_data["contact_email"]
                    )

                supplier = suppliers[supplier_id]

                if item["type"] == "physical":
                    product = ProductFactory.create(
                        "physical",
                        item["id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        supplier,
                        weight=item["weight"]
                    )

                elif item["type"] == "digital":
                    product = ProductFactory.create(
                        "digital",
                        item["id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        supplier,
                        download_size=item["download_size"]
                    )

                else:
                    raise ValueError("Unknown product type.")

                loaded_products.append(product)

            self.products = loaded_products
            print("Inventory loaded successfully.")

        except (ValueError, KeyError, TypeError, OSError) as error:
            print("Error loading inventory:", error)
