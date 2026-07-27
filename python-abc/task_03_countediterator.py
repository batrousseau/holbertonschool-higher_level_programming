#!/usr/bin/python3


"""Module providing an iterator that counts items during iteration.

This module defines the CountedIterator class which wraps
any iterable object and tracks the number of times __next__
is called, returning a count accessible via get_count()."""


class CountedIterator():
    """An iterator subclass that increments a counter
    on each call to next().

    This class initializes with an iterable object,
    creates its own iterator instance, and maintains a private-like attribute
    'count' updated every time __next__ is invoked."""

    def __init__(self, obj):
        self.iterator = iter(obj)
        self.count: int = 0

    def get_count(self):
        """Return the current iteration count.

        This method returns the value of the instance attribute
        'count' which tracks how many times next() has been called
        since initialization."""

        return self.count

    def __iter__(self):
        return self

    def __next__(self):
        """Advance iterator and increment counter before returning next item.

        Increments internal counter, retrieves next element
        from wrapped iterator, then returns the value to caller
        without modifying count logic further."""

        value = next(self.iterator)
        self.count += 1
        self.get_count()
        return (value)
