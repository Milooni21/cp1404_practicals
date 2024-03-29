import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1
MAX_PRICE = 100
INITIAL_PRICE = 10.0
OUT_FILE = "stock_prices.txt"

def main():
    price = INITIAL_PRICE

    day_number = 1
    out_file = open(OUT_FILE, "w")

    print("Starting price is ${:,.2f}".format(price), file=out_file)

    while price >= MIN_PRICE and price <= MAX_PRICE:
        price_change = 0
        # generate a random integer of 1 or 2
        # if it's 1, the price increases, otherwise it decreases
        if random.randint(1, 2) == 1:
            # generate a random floating-point number
            # between 0 and MAX_INCREASE
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            # generate a random floating-point number
            # between negative MAX_DECREASE and 0
            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)
        print("On day {} price is: ${:,.2f}".format(day_number, price), file=out_file)
        day_number += 1

    out_file.close()


main()





