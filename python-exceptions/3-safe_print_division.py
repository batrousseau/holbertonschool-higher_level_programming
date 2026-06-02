#!/usr/bin/python3

def safe_print_division(a, b):
    result: int = int()

    try:
        result = a/b
    except ValueError:
        result = None
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)
