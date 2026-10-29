
FROM python:3.14-slim

WORKDIR /app

COPY inventory_manager.py .
COPY inventory.py .
COPY product.py .

CMD ["python", "inventory_manager.py"]
