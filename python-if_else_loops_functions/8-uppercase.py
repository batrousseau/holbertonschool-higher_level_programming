#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        n = ord(str[i])
        print("{}".format(chr(n-32) if n > 96 and n < 123 else str[i]), end="")
    print("")
