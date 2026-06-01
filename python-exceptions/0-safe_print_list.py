#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    number_printed: int = int()
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            number_printed = number_printed + 1
        except ValueError:
            i = + 1
        except IndexError:
            break
    print()
    return (number_printed)
