def main():
    number_of_items = int(input("Number of items: "))
    total_price = 0
    while number_of_items < 0:
        print("Invalid items! Please enter again.")
        number_of_items = int(input("Number of items: "))
    for i in range(number_of_items):
        price_of_items = float(input("Price of item: "))
        total_price += price_of_items

    if total_price > 100:
        print("Total price for {} items is ${:.2f}".format(number_of_items,total_price * 0.9))
    else:
        print("Total price for {} items is ${:.2f}".format(number_of_items,total_price))


main()