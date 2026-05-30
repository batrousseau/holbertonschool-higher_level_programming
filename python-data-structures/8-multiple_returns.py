#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    else:
        lenght: int = len(sentence)
        first: str = sentence[:1]
        return (lenght, first)
