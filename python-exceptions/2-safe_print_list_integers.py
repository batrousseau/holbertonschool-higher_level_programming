#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    hm_printed: int = int()
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            hm_printed = hm_printed + 1
        except ValueError:
            i = i + 1
        except TypeError:
            break
    print()
    return (hm_printed)
