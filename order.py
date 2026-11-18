from product import Product
from order_line import OrderLine
from discount_strategy import DiscountStrategy, NoDiscount


class Order:
    def __init__(
        self,
        order_id: str,
        discount: DiscountStrategy | None = None
    ) -> None:
        self.order_id = order_id
        self.order_lines: list[OrderLine] = []
        self.discount = discount if discount is not None else NoDiscount()

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

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
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)

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
