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

    def to_json(self):
        """Return the internal dictionary
        representation of this student.

        Retrieves all instance attributes via __dict__
        and returns them as a plain Python dict object for
        serialization or inspection purposes."""

        return self.__dict__
