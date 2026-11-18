import csv

from inventory import Inventory
from product_factory import ProductFactory
from supplier import Supplier


def load_products(
    path: str,
    inventory: Inventory,
    supplier: Supplier
) -> None:
    loaded = 0

    try:
        file = open(path, newline="", encoding="utf-8")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        with file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                try:
                    product_type, product_id, name, price, stock = row

                    product = ProductFactory.create(
                        product_type,
                        product_id,
                        name,
                        float(price),
                        int(stock),
                        supplier
                    )

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as error:
                    print(f"Skipping row {row}: {error}")

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")
