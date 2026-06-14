#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    if not my_list_1 or not my_list_2:
        return (None)
    new_list: list = []

    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            new_list.append(0)
            print("out of range")
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except TypeError:
            new_list.append(0)
            print("wrong type")
        finally:
            continue

    return (new_list)
