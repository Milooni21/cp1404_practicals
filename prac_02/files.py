def program_1():
    out_file = open("name.txt", "w")
    name = input("Please enter your name: ")
    print(name, file=out_file)
    out_file.close()

program_1()

def program_2():
    in_file = open("name.txt", "r")
    name = in_file.read().strip()
    in_file.close()
    print("Your name is", name)

program_2()

def program_3():
    number_file = open("numbers.txt", "r")
    number1 = int(number_file.readline())
    number2 = int(number_file.readline())
    number_file.close()
    print(number1 + number2)

program_3()

def program_4():
    number_file = open("numbers.txt", "r")
    total = 0
    for line in number_file:
        number = int(line)
        total += number
    number_file.close()
    print(total)

program_4()


