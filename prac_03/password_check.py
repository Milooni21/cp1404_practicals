MINIMUM_LENGTH = 4

def version_1():
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    print("*" * len(password))

# version_1()

def main():
    """Get and print password using functions"""
    password = get_password(MINIMUM_LENGTH)
    print_asterisk(password)


def get_password(minimum_length):
    password = input("Enter password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Password is too short. Please enter again.")
        password = input("Enter password of at least {} characters: ".format(minimum_length))
    return password

def print_asterisk(sequence):
    print("*" * len(sequence))

main()
