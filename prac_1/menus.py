"""
get the input number of items
get the total price
get the input prices of each item and calculate total price
Apply discount if total price is over $100
Apply 10% discount
Display total price
"""
# CODE:


def main():
    num_items = -1
    while num_items < 0:
        num_items = int(input("Number of items: "))
        if num_items < 0:
            print("Invalid number of items!")

    total_price = 0

    for i in range(num_items):
        price = float(input("Price of item {}: ".format(i + 1)))
        total_price += price

    if total_price > 100:
        total_price *= 0.9

    print("Total price for", num_items, "items is $" + "{:.2f}".format(total_price))


if __name__ == "__main__":
    main()
