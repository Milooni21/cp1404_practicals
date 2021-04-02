import random
def main():
    print(random.randint(5, 20))
    # the smallest number was 5 and the largest number was 20

    print(random.randrange(3, 10, 2))
    # the smallest number was 3 and the largest number was 9
    # the line 2 cannot produced 4

    print(random.uniform(2.5, 5.5))
    # the smallest number was 2.5 and the largest number was 5.5

    print(random.randint(1, 100))


main()