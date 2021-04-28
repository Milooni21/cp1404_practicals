from prac_06.guitar import Guitar

CURRENT_YEAR = 2021


def run_tests():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2013, 1512.9)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 99, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 8, other.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name, False, other.is_vintage()))


if __name__ == '__main__':
    run_tests()