inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity or type quit: ")

    if stock == "quit":
        break
    elif stock.isdigit():
        quantity = int(stock)
        inventory = inventory + quantity
        print("Current inventory:", inventory)
    else:
        print("Invalid stock quantity")
        failed_entries = failed_entries + 1