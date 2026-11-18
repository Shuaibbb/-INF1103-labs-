from inventory import Inventory
from product_factory import ProductFactory
from supplier import Supplier


def add_product(inventory: Inventory) -> None:
    print("\nAdd New Product")
    print("1. Physical Product")
    print("2. Digital Product")

    product_type = input("Select product type: ")

    if product_type not in ("1", "2"):
        print("Invalid product type.")
        return

    product_id = input("Product ID: ").strip()

    if inventory.find_product(product_id) is not None:
        print("Product ID already exists.")
        return

    name = input("Product Name: ").strip()

    print("\nSupplier Details")
    supplier_id = input("Supplier ID: ").strip()
    supplier_name = input("Supplier Name: ").strip()
    supplier_email = input("Supplier Email: ").strip()

    if not supplier_id or not supplier_name or not supplier_email:
        print("All supplier fields are required.")
        return

    # Reuse an existing supplier if the ID matches
    supplier = None

    for existing_product in inventory.products:
        if existing_product.supplier.supplier_id == supplier_id:
            supplier = existing_product.supplier
            break

    if supplier is None:
        supplier = Supplier(
            supplier_id, supplier_name, supplier_email
        )

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        if not product_id or not name:
            print("Product ID and name cannot be empty.")
            return

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

        if product_type == "1":
            weight = float(input("Weight (kg): "))

            if weight < 0:
                print("Weight cannot be negative.")
                return

            product = ProductFactory.create(
                "physical", product_id, name, price, 
                stock,supplier, weight=weight
            )

        else:
            download_size = float(
                input("Download Size (MB): ")
            )

            if download_size < 0:
                print("Download size cannot be negative.")
                return

            product = ProductFactory.create(
                "digital", product_id, name, price,
                stock, supplier, download_size=download_size
            )

        inventory.add_product(product)

    except ValueError as error:
        print("Invalid input:", error)


def update_stock(inventory: Inventory) -> None:
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip()

    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product:", product.name)
    print("Current Stock:", product.stock)

    try:
        new_stock = int(input("New Stock Quantity: "))
        inventory.update_stock(product_id, new_stock)

    except ValueError as error:
        print("Invalid stock quantity:", error)


def search_product(inventory: Inventory) -> None:
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()

    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("\nProduct Found")
    print("--------------------------------")
    product.display_information()
    print("Fulfilment:", product.get_fulfilment_info())
    print("--------------------------------")


def main() -> None:
    inventory = Inventory()

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Load Inventory")
        print("7. Exit")
        print("----------------------------")

        option = input("Enter option: ").strip()

        if option == "1":
            inventory.display_all()

        elif option == "2":
            add_product(inventory)

        elif option == "3":
            update_stock(inventory)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            inventory.save_inventory()

        elif option == "6":
            inventory.load_inventory()

        elif option == "7":
            print("Saving inventory before exit...")
            inventory.save_inventory()
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
