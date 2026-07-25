from abc import ABC, abstractmethod


"""Module defining an abstract base class for animals and their subclasses.

This module implements simple inheritance hierarchy where each animal subclass
must implement the 'sound' method to return its specific vocalization."""


class Animal(ABC):
    """Abstract base class representing any kind of animal with sound.

    This class defines abstract method 'sound' that must be implemented by all
    concrete subclasses, ensuring each provides a unique output"""

    @abstractmethod
    def sound(self):
        """Return the specific sound made by this animal type.

        Subclasses must override to return their vocalization string.
        The base implementation is abstract, cannot be instantiated directly"""


class Dog(Animal):
    """Concrete subclass representing a dog that barks when making noise."""

    def sound(self):
        """Return the bark sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Concrete subclass representing a cat that Meow when making noise."""
    def sound(self):
        """Return the Meow sound of a cat."""
        return "Meow"
