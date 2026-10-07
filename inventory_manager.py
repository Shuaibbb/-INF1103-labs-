import json
import os

def load_inventory():
    if os.path.exists("inventory.json"):
        file = open("inventory.json", "r")
        products = json.load(file)
        file.close()

        print("inventory.json found.")
        print("Inventory loaded successfully.")
        return products
    else:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")
        return []

def display_all(products):
    print("\nCurrent Inventory")
    print("------------------------------------------------")

    for product in products:
        print(
            "ID:", product["id"],
            "| Name:", product["name"],
            "| Price: $" + format(product["price"], ".2f"),
            "| Stock:", product["stock"]
        )

    print("------------------------------------------------")


inventory = load_inventory()
display_all(inventory)