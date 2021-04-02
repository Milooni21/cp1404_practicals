# display odd bumbers between 1 and 20

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# (a)
for i in range(0,101,10):
    print(i)
print()

# (b)
for i in range(20,0,-1):
    print(i)
print()

# (c)

number_of_stars = int(input("Enter number of stars: "))
for i in range(number_of_stars):
    print("*", end="")
print()

# (d)

for i in range(1, number_of_stars +1):
    print("*" * i)
print()
