#!/usr/bin/python3

import requests
import csv


"""Module providing utilities to fetch JSON
data from an API and process it.

This module defines functions to retrieve posts
from a public endpoint, print their titles or save
them into a CSV file with error handling for missing files."""


def fetch_and_print_posts():
    """Fetch all posts from the API and print
    only their 'title' fields.

    Sends GET request retrieves JSON response
    iterates over list checks each key prints value matching
    title variable name handles potential errors implicitly
    via json parsing logic flow execution path here only."""

    r = requests.get("https://jsonplaceholder.typicode.com/posts/")
    print(f"{r.status_code}")
    json_list = r.json()
    variable: str = "title"
    for element in json_list:
        for key in element.keys():
            if key == variable:
                print(f"{element.get(key)}")


def fetch_and_save_posts():
    """Fetch all posts and save them to a
    CSV file with error handling.

    Sends GET request retrieves JSON response
    opens target path writes header row then iterates
    rows using DictWriter handles FileNotFoundError
    PermissionError OSError by printing messages returning False on failure."""

    r = requests.get("https://jsonplaceholder.typicode.com/posts/")
    json_list = r.json()


    try:
        with open("posts.csv", mode="w", encoding="utf-8") as file:
            csv_dict = csv.DictWriter(file, fieldnames=["userId","id", "title", "body"])
            csv_dict.writeheader()
            csv_dict.writerows(json_list)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{r}' est introuvable.")
        return False
    except (PermissionError, OSError) as e:
            print(f"Erreur d'accès au fichier : {e}")
            return False
