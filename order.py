
from product import Product
from order_line import OrderLine


class Order:
    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, index: int) -> None:
        if 0 <= index < len(self.order_lines):
            self.order_lines.pop(index)
            print("Order line removed.")
        else:
            print("Invalid order line index.")

    def calculate_total(self) -> float:
        total = 0.0

        for line in self.order_lines:
            total += line.calculate_subtotal()

        return total

    def display_order(self) -> None:
        print("\nOrder ID:", self.order_id)
        print("----------------------------------------")

        for line in self.order_lines:
            print(
                "Product:", line.product.name,
                "| Quantity:", line.quantity,
                "| Subtotal: $" + format(line.calculate_subtotal(), ".2f")
            )

        print("Total: $" + format(self.calculate_total(), ".2f"))
