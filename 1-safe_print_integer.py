#!/usr/bin/python3

def safe_print_integer(value):
    be_printed: bool = bool()
    try:
        print("{:d}".format(value))
        be_printed = True
    except ValueError:
        be_printed = False
    except AttributeError:
        be_printed = False
    finally:
        return (be_printed)
