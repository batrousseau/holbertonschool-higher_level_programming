#!/usr/bin/python3

def print_last_digit(number):
    lst_digit = 0
    if number >= 0:
        lst_digit = number % 10
    else:
        lst_digit = (number % -10) * -1
    print("{}".format(lst_digit), end="")
    return (lst_digit)
