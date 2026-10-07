inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25
    }
]


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


display_all(inventory)