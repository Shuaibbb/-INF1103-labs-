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


def calculate_tax(amount):
    tax = amount * 0.10
    return tax


def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


inventory = 0
failed_entries = 0
deliveries_processed = 0

while True:
    stock = get_valid_input()

    if stock == "quit":
        break
    elif stock is None:
        failed_entries = failed_entries + 1
    else:
        inventory = process_delivery(inventory, stock)
        deliveries_processed = deliveries_processed + 1
        tax = calculate_tax(stock)

        print("Current inventory:", inventory)
        print("Tax for this delivery:", tax)

        if inventory > 500:
            print("Overstock alert")
            break

print("Total Deliveries Processed:", deliveries_processed)
generate_report(inventory, failed_entries)