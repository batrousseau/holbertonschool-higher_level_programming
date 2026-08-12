#!/usr/bin/env python3
from task_03_countediterator import CountedIterator


def print_section(title):
    print(f"\n--- {title} ---")


# =====================================================================
# TEST 1 : Boucle 'for' standard et vérification du protocole (__iter__)
# =====================================================================
print_section("Test 1: Utilisation dans une boucle 'for'")
data_list = ["a", "b", "c"]
ci1 = CountedIterator(data_list)

# Vérification primordiale : iter(ci) doit renvoyer ci lui-même !
if iter(ci1) is ci1:
    print("✅ Protocole OK : iter(ci) renvoie bien l'objet lui-même.")
else:
    print("❌ Erreur : __iter__() ne renvoie pas 'self'.")

for item in ci1:
    print(f"Élément : {item} | Compteur actuel : {ci1.get_count()}")

print(f"Compteur final (attendu: 3) : {ci1.get_count()}")


# =====================================================================
# TEST 2 : Structure vide
# =====================================================================
print_section("Test 2: Données vides")
ci_empty = CountedIterator([])

try:
    next(ci_empty)
    print("❌ Erreur : Il aurait dû y avoir un StopIteration.")
except StopIteration:
    print("✅ StopIteration levé immédiatement.")

print(f"Compteur final sur vide (attendu: 0) : {ci_empty.get_count()}")


# =====================================================================
# TEST 3 : Insistance après épuisement (Post-StopIteration)
# =====================================================================
print_section("Test 3: Appels répétitifs à next() une fois épuisé")
ci_short = CountedIterator([42])

first_val = next(ci_short)
print(f"Première valeur : {first_val} | Compteur : {ci_short.get_count()}")

# On force l'épuisement
try:
    next(ci_short)
except StopIteration:
    print("✅ Premier StopIteration attrapé.")

# Si on réessaie encore de faire next(), le compteur NE DOIT PAS augmenter !
try:
    next(ci_short)
except StopIteration:
    print("✅ Second StopIteration attrapé.")

print(
    f"Compteur après plusieurs StopIteration (attendu: 1) : {ci_short.get_count()}"
)


# =====================================================================
# TEST 4 : Types de données variés (Générateurs, Chaînes, Sets, Range)
# =====================================================================
print_section("Test 4: Types d'itérables non-listes")

# Test avec une chaîne de caractères
ci_str = CountedIterator("Py")
print(
    f"String -> Extrait : {[next(ci_str), next(ci_str)]} | Compteur : {ci_str.get_count()}"
)

# Test avec un générateur / range
ci_range = CountedIterator(range(100, 105))
print(f"Range -> Extrait : {next(ci_range)} | Compteur : {ci_range.get_count()}")


# =====================================================================
# TEST 5 : Utilisation mixte (next() manuels + reprise en boucle for)
# =====================================================================
print_section("Test 5: Lecture mixte (next() puis boucle for)")
ci_mix = CountedIterator([10, 20, 30, 40, 50])

print(f"Manual next: {next(ci_mix)}")  # Consomme 10
print(f"Manual next: {next(ci_mix)}")  # Consomme 20
print(f"Compteur à mi-parcours (attendu: 2) : {ci_mix.get_count()}")

print("Reprise du reste avec une boucle for :")
for val in ci_mix:  # Doit reprendre à 30
    print(f"  Reste : {val}")

print(f"Compteur final (attendu: 5) : {ci_mix.get_count()}")
