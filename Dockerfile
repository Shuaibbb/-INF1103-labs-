FROM python:3.14-slim

WORKDIR /app

COPY inventory_manager.py .
COPY inventory.py .
COPY product.py .
COPY supplier.py .
COPY order.py .
COPY order_line.py .
COPY discount_strategy.py .
COPY product_factory.py .
COPY input_helpers.py .
COPY csv_loader.py .
COPY products.csv .
COPY tests/ ./tests/

CMD ["python", "inventory_manager.py"]
