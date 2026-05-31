#!/usr/bin/python3

def best_score(a_dictionary):
    winner: str = ""
    score: int = int()
    if not a_dictionary:
        return (None)
    for key, value in a_dictionary.items():
        if value > score:
            score = value
            winner = key
    return (winner)
