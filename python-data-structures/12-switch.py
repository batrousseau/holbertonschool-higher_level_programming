#!/usr/bin/python3

if __name__ == "__main__":
    a = 89
    b = 10

    temp: int = a
    a = b
    b = temp

    print("a={:d} - b={:d}".format(a, b))
