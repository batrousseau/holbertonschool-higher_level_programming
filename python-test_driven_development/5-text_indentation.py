#!/usr/bin/python3

"""
This modules is accurately depicted by this description.
It contains an awesome function which will be detailled
in the dedicated comment section of the function.
Some might says the documentation of a module containing one
function is though not very usefull.

Well you don't always do what you want ok ?
"""


def text_indentation(text):
    """
    text_indentation - add two blanckline after
    each  of the following character ":" "?" "."
    and print the new string
    text: a string that will be indented
    Return: Nothing
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    if text == "":
        return
    char: list = [":", "?", "."]
    start_index = 0
    for index in range(len(text)):
        for char_whole in char:
            if text[index] == char_whole:
                new_string: str = text[start_index:index + 1].strip()
                print(new_string, end="")
                print("\n")
                start_index = index + 1
    if start_index == 0:
        print(text, end="")
