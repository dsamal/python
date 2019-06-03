__author__ = 'DEBASISH'


# This is a utility script which has multiple small utility functions to test and practice

# Fibonacci Series:
# The sum of two elements defines the next
def print_fibonacci():
    n = int(input("Please enter the number till which you want to print the fibonaci series:"))
    print("Well, here yo go", end=":")
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print("", "Thank You!")


def print_even_numbers():
    n = int(input("Please enter the numbers between which you want to display the even numbers: "))
    m = int(input(": "))
    print("Well you entered", n, "&", m)
    print("Well the even numbers between", n, "and", m, "are: ")
    if n % 2 != 0:
        n = n + 1
    while n < m:
        print(n, end="  ")
        n = n + 2

    print("\n", "Thank You!")


def select_utility(ip):
    if ip == 0:
        print("Thanks for using the Utility Management Tool, b bye!")
    elif ip == 1:
        print_fibonacci()
    elif ip == 2:
        print_even_numbers()
    else:
        print("To be Implemented")


def display_input_options():
    x = -1
    print("========== Welcome to Utility Management Tool ==========")
    while x < 0 or x > 10:
        print("Please select from the following Menu\n\
        # To print fibonacci series enter: 1 \n\
        # To print even numbers enter: 2 \n\
        # To print odd numbers enter: 3 \n\
        # If you want to know current date and time enter: 4\n\
        # To exit enter : 0 \n\
        ")
        x = int(input("Which Utility You Want to Use :"))
        print("You entered: ", x)

    return x


user_input = display_input_options()
select_utility(user_input)
