def get_valid_input():
    stock = input("Enter stock quantity or type quit: ")

    if stock == "quit":
        return "quit"
    elif stock.isdigit():
        return int(stock)
    else:
        print("Invalid stock quantity")
        return None


def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


inventory = 0
failed_entries = 0

while True:
    stock = get_valid_input()

    if stock == "quit":
        break
    elif stock is None:
        failed_entries = failed_entries + 1
    else:
        inventory = process_delivery(inventory, stock)
        print("Current inventory:", inventory)

        if inventory > 500:
            print("Overstock alert")
            break

print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)