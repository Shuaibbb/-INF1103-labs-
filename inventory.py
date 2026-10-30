
import json
import os
from product import Product


class Inventory:
    def __init__(self):
        self.products = []
        self.load_inventory()

    def display_all(self):
        print("\nCurrent Inventory")
        print("----------------------------------------")

        if len(self.products) == 0:
            print("Inventory is empty.")
        else:
            for product in self.products:
                print()
                product.display_information()

        print("----------------------------------------")

    def add_product(self, product):
        if self.search_product(product.product_id) is not None:
            print("Product ID already exists.")
            return

        self.products.append(product)
        print("Product added successfully!")

    def search_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product

        return None

    def update_stock(self, product_id, new_stock):
        product = self.search_product(product_id)

        if product is not None:
            product.update_stock(new_stock)
            print("Stock updated successfully!")
        else:
            print("Product not found.")

    def save_inventory(self):
        data = []

        for product in self.products:
            data.append({
                "id": product.product_id,
                "name": product.name,
                "price": product.price,
                "stock": product.stock
            })

        with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Inventory saved successfully.")

    def load_inventory(self):
        if not os.path.exists("inventory.json"):
            print("Starting with an empty inventory.")
            return

        try:
            with open("inventory.json", "r") as file:
                data = json.load(file)

            loaded_products = []

            for item in data:
                product = Product(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"]
                )
                loaded_products.append(product)

            self.products = loaded_products
            print("Inventory loaded successfully.")

        except (ValueError, KeyError, TypeError, OSError) as error:
            print("Error loading inventory:", error)
