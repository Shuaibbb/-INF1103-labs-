
import json
import os
from product import PhysicalProduct, DigitalProduct


class Inventory:
    def __init__(self):
        self.products = []
        self.load_inventory()

    def display_all(self):
        print("\nCurrent Inventory")
        print("------------------------------------------------")

        if len(self.products) == 0:
            print("Inventory is empty.")
        else:
            for product in self.products:
                print()
                product.display_information()

        print("------------------------------------------------")

    def add_product(self, product):
        for existing in self.products:
            if existing.product_id == product.product_id:
                print("Product ID already exists.")
                return

        self.products.append(product)
        print("Product added successfully!")

    def update_stock(self, product_id, new_stock):
        product = self.search_product(product_id)

        if product is not None:
            product.update_stock(new_stock)
            print("Stock updated successfully!")
        else:
            print("Product not found.")

    def search_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product

        return None

    def save_inventory(self):
        data = []

        for product in self.products:
            product_data = {
                "id": product.product_id,
                "name": product.name,
                "price": product.price,
                "stock": product.stock
            }

            if isinstance(product, PhysicalProduct):
                product_data["type"] = "physical"
                product_data["weight"] = product.weight

            elif isinstance(product, DigitalProduct):
                product_data["type"] = "digital"
                product_data["download_size"] = product.download_size

            data.append(product_data)

        with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Inventory saved successfully to inventory.json.")

    def load_inventory(self):
        if not os.path.exists("inventory.json"):
            print("inventory.json not found.")
            print("Starting with an empty inventory.")
            return

        try:
            with open("inventory.json", "r") as file:
                data = json.load(file)

            loaded_products = []

            for item in data:
                product_type = item.get("type", "physical")

                if product_type == "physical":
                    product = PhysicalProduct(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item.get("weight", 0)
                    )

                elif product_type == "digital":
                    product = DigitalProduct(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["download_size"]
                    )

                else:
                    print("Unknown product type:", product_type)
                    continue

                loaded_products.append(product)

            self.products = loaded_products

            print("inventory.json found.")
            print("Inventory loaded successfully.")

        except (ValueError, KeyError, TypeError, OSError) as error:
            print("Error loading inventory:", error)
