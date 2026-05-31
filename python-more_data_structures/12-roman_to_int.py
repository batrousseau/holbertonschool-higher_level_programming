#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or isinstance(roman_string, str) is False:
        return (0)
    # I Start by adding all the symbols
    thousand: int = roman_string.count("M") * 1000
    five_hundred: int = roman_string.count("D") * 500
    hundred: int = roman_string.count("C") * 100
    fifty: int = roman_string.count("L") * 50
    ten: int = roman_string.count("X") * 10
    five: int = roman_string.count("V") * 5
    one: int = roman_string.count("I") * 1

    posit: int = thousand + five_hundred + hundred + fifty + ten + five + one
    # I treat the substractive case
    sub_2: int = (roman_string.count("IV") + roman_string.count("IX")) * 2
    sub_20: int = (roman_string.count("XL") + roman_string.count("XC")) * 20
    sub_200: int = (roman_string.count("CD") + roman_string.count("CM")) * 200

    negative: int = sub_2 + sub_20 + sub_200
    # It adds up
    result: int = posit - negative
    return (result)
