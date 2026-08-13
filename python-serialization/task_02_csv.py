#!/usr/bin/python3

import csv
import json

def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, mode="r",newline='',encoding="utf-8") as file:
            data = list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file}' est introuvable.")
        return False
    except (PermissionError, OSError) as e:
        print(f"Erreur d'accès au fichier : {e}")
        return False

    try:
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data,json_file, indent=4)
            return True
    except (EOFError, AttributeError, ImportError) as e:
            print(f"Erreur de désérialisation : fichier corrompu ou incomplet ({e})")
