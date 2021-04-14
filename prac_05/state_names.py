def main():
    CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                    "NT": "Northern Territory", "WA": "Western Australia",
                    "ACT": "Australian Capital Territory", "VIC": "Victoria",
                    "TAS": "Tasmania"}

    state = input("Enter short state: ").upper()
    while state != "":
        if state in CODE_TO_NAME:
            print(state, "is", CODE_TO_NAME[state])
        else:
            print("Invalid short state")
        state = input("Enter short state: ").upper()

    # Write a loop that prints all of the states and names neatly lined up with string formatting.

    for key, value in CODE_TO_NAME.items():
        print(key, "is", value)


main()
