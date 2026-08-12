#!/usr/bin/python3

import pickle

class CustomObject():

    @classmethod 
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            
        # Validation de type défensive après lecture
            if not isinstance(obj, cls):
                raise TypeError(f"Le fichier ne contient pas un {cls.__name__}")
            
            return obj

        except FileNotFoundError:
            print(f"Erreur : Le fichier '{filename}' est introuvable.")
        except (PermissionError, OSError) as e:
            print(f"Erreur d'accès au fichier : {e}")
        except (pickle.UnpicklingError, EOFError, AttributeError, ImportError) as e:
            print(f"Erreur de désérialisation : fichier corrompu ou incomplet ({e})")
        except TypeError as e:
            print(f"Erreur de contenu : {e}")
        
        return None

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("name doit être une chaîne de caractères")
        self._name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if not isinstance(value, int):
            raise TypeError("age doit être un entier")
        if value < 0:
            raise ValueError("age ne peut pas être négatif")
        self._age = value


    @property
    def is_student(self) -> bool:
        return self._is_student

    @is_student.setter
    def is_student(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("is_student doit être un booléen")
        self._is_student = value

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs student: {self.is_student}\n")

    def serialize(self, filename):
        with open(filename, mode="wb") as file:
            pickle.dump(self, file)
