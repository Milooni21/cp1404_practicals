"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
---> It will occur when the function's argument is an inappropriate type eg:- string, float
2. When will a ZeroDivisionError occur?
---> It occurs when the denominator is divided by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
---> no, you cannot
"""

def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")

main()