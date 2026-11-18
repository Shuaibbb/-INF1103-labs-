
import unittest
import tempfile
from pathlib import Path

from supplier import Supplier
from product_factory import ProductFactory
from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount
)
from order import Order
from order_line import OrderLine
from inventory import Inventory
from csv_loader import load_products
from input_helpers import get_positive_float
from unittest.mock import patch


class TestLab9(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "Tech Supplier", "tech@example.com"
        )
        self.product = ProductFactory.create(
            "physical", "P001", "Laptop", 100, 10,
            self.supplier, weight=2.0
        )

    def test_discount_strategies(self):
        self.assertEqual(NoDiscount().apply(250), 250)
        self.assertEqual(PercentageDiscount(10).apply(250), 225)
        self.assertEqual(BulkDiscount(200, 20).apply(250), 230)
        self.assertEqual(StudentDiscount().apply(250), 237.5)

    def test_order_discount_switching(self):
        order = Order("O001")
        order.add_order_line(self.product, 2)

        self.assertEqual(order.calculate_total(), 200)

        order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(order.calculate_total(), 180)

        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 180)

    def test_factory(self):
        physical = ProductFactory.create(
            "physical", "P002", "Mouse", 25, 5,
            self.supplier, weight=0.2
        )
        digital = ProductFactory.create(
            "digital", "D001", "Software", 50, 10,
            self.supplier, download_size=500
        )

        self.assertEqual(type(physical).__name__, "PhysicalProduct")
        self.assertEqual(type(digital).__name__, "DigitalProduct")

    def test_unknown_product_type(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "service", "S002", "Installation",
                30, 5, self.supplier
            )

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P003", "Invalid",
                0, 5, self.supplier, weight=1
            )

    def test_negative_stock(self):
        with self.assertRaises(ValueError):
            self.product.update_stock(-1)

    def test_invalid_order_quantity(self):
        with self.assertRaises(ValueError):
            OrderLine(self.product, 0)

    def test_positive_float_input(self):
        with patch(
            "builtins.input",
            side_effect=["abc", "-5", "12.50"]
        ):
            result = get_positive_float("Price: ")

        self.assertEqual(result, 12.5)

    def test_csv_loading(self):
        with tempfile.TemporaryDirectory() as folder:
            folder_path = Path(folder)

            inventory = Inventory(
                str(folder_path / "inventory.json")
            )

            csv_file = folder_path / "products.csv"
            csv_file.write_text(
                "product_type,product_id,name,price,stock_quantity\n"
                "physical,P001,Desk Lamp,25.00,10\n"
                "digital,D001,Photo Editor,49.90,100\n"
                "service,S001,Installation,30.00,5\n"
                "physical,P002,Office Chair,abc,3\n"
                "physical,P003,Monitor Stand,39.50,7\n",
                encoding="utf-8"
            )

            load_products(
                str(csv_file), inventory, self.supplier
            )

            self.assertEqual(len(inventory.products), 3)

    def test_missing_csv_file(self):
        with tempfile.TemporaryDirectory() as folder:
            inventory = Inventory(
                str(Path(folder) / "inventory.json")
            )

            missing_file = str(
                Path(folder) / "missing.csv"
            )

            load_products(
                missing_file, inventory, self.supplier
            )

            self.assertEqual(len(inventory.products), 0)


if __name__ == "__main__":
    unittest.main()
