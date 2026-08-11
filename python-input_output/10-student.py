#!/usr/bin/python3


"""Module providing a Student class for managing student information data.

This module defines the Student class which stores first name,
last_name and age attributes with methods to serialize instance state."""


class Student():
    """A simple class representing a student entity
    with basic personal details.

    This class initializes an object with three mandatory
    fields: first_name, last_name and age. It provides a method
    to return the internal dictionary representation of
    its current state directly."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance with provided
        personal details.

        Sets private attributes for first name, last name
        and age values passed during object creation process
        flow execution path here only."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a filtered dictionary based
        on provided attribute names.

        If 'attrs' is None returns full instance __dict__.
        Otherwise iterates over specified attributes and builds
        new dict containing only those that exist as
        valid keys in current object state."""

        custom_dict: dict = {}
        if attrs is not None:
            for attr in attrs:
                try:
                    custom_dict[attr] = getattr(self, attr)
                except AttributeError:
                    pass
            return custom_dict
        else:
            return self.__dict__
