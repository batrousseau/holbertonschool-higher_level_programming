#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    #creating mutables int
    a0: int = 0
    a1: int = 0
    b0: int = 0
    b1: int = 0
    #checking for NULL value in a then in B
    if not tuple_a:
        return(tuple_b)
    if not tuple_b:
        return(tuple_a)
    #checking for minimum lenght of each tuple
    if len(tuple_a) < 2:
        a0 = tuple_a[0]
    if len(tuple_a) == 2:
        a0 = tuple_a[0]
        a1 = tuple_a[1]
    if len(tuple_b) < 2:
        b0 = tuple_b[0]
    if len(tuple_b) == 2:
        b0 = tuple_b[0]
        b1 = tuple_b[1]
    tuple_c = ((a0 + b0), (a1 + b1))
    return(tuple_c)
