#!/usr/bin/python3


"""Module providing a list subclass with sorting capabilities.
This module defines the MyList class, which inherits from
the built-in list type.
It adds functionality to print the contents of the list in sorted order without
modifying the original instance.
"""


class MyList(list):
    """A list subclass that can print its sorted version."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying it.

        Creates a copy of the current list, sorts it, and prints the result.
        The original list remains unchanged after this operation is completed.
        """
        new_list: list = self.copy()
        new_list.sort()
        print(f"{new_list}")
