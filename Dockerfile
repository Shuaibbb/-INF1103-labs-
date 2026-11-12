
FROM python:3.14-slim

WORKDIR /app

COPY inventory_manager.py .
COPY inventory.py .
COPY product.py .
COPY supplier.py .
COPY order.py .
COPY order_line.py .

CMD ["python", "inventory_manager.py"]
