#!/usr/bin/python3

def print_last_digit(number):
    last_digit = (abs(number) % 10)  # Get the remainder of the absolute number when divided by 10
    print(last_digit, end="")
    return last_digit
