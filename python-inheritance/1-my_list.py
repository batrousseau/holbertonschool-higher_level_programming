#!/usr/bin/python3


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
