#!/usr/bin/python3


"""Module providing a verbose list subclass with detailed logging actions.

This module defines the VerboseList class which extends built-in list
to print messages upon appending, extending or removing items, and includes
utility functions for type checking."""


class VerboseList(list):
    """A list subclass that prints notifications when modifying its contents.

    This class overrides standard list methods like append, extend,
    remove and pop to provide verbose feedback about each operation
    performed on the instance."""

    def append(self, value):
        """Append a single item to the end of this VerboseList
        with logging.

        Calls parent method then prints confirmation message
        showing added value."""
        try:
            super().append(value)
        except TypeError:
            return
        print(f"Added [{value}] to the list.")

    @staticmethod
    def isiterable(obj):
        """Check if an object supports iteration without consuming it.

        Attempts to call iter() on obj and returns True if successful,
        False otherwise."""
        try:
            iter(obj)
            return (True)
        except TypeError:
            return (False)

    def extend(self, iterable):
        """Extend the list with items from an iterable object
        after validation.

        Validates that input is iterable before extending and
        prints count of added items."""

        if VerboseList.isiterable(iterable) is False:
            raise TypeError(f"{iterable} must be an interable.")
        try:
            super().extend(iterable)
        except TypeError:
            return

        print(f"Extend the list with [{len(iterable)}] items.")

    def remove(self, value):

        for item in self:
            if item == value:
                try:
                    super().remove(value)
                    print(f"Removed [{value}] from the list.")
                    return
                except TypeError:
                    return

        print(f"{value} is not in {self}")

    def pop(self, index=-1):
        """Remove and return item at specified
        index with logging.

        Handles IndexError gracefully by returning
        None if no element exists."""

        try:
            value = self[index]
            super().pop(index)
            print(f"Popped [{value}] from the list")
            return (value)
        except IndexError:
            return
