#!/usr/bin/env python3
import io
import sys
from task_04_flyingfish import Fish, Bird, FlyingFish


def capture_output(func, *args, **kwargs):
    """Utilitaire pour capturer la sortie stdout d'une fonction."""
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        func(*args, **kwargs)
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdout = old_stdout


def print_test(name, success, details=""):
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"{status} | {name}")
    if not success and details:
        print(f"      └── ⚠️  {details}")


print("=" * 60)
print("  STRESS TEST : HÉRITAGE MULTIPLE (FlyingFish / Fish / Bird)")
print("=" * 60)

# ---------------------------------------------------------------------
# TEST 1 : Isolation des classes mères (Rien ne doit être pollué)
# ---------------------------------------------------------------------
print("\n--- 1. Test d'isolation des classes mères ---")
f = Fish()
b = Bird()

f_swim = capture_output(f.swim)
b_fly = capture_output(b.fly)
f_hab = capture_output(f.habitat)
b_hab = capture_output(b.habitat)

print_test("Fish() conserve son swim original", "swimming" in f_swim.lower() and "flying fish" not in f_swim.lower(), f"Obtenu: '{f_swim}'")
print_test("Bird() conserve son fly original", "flying" in b_fly.lower() or "soaring" in b_fly.lower(), f"Obtenu: '{b_fly}'")
print_test("Fish.habitat() est resté intact", "water" in f_hab.lower() and "sky" not in f_hab.lower(), f"Obtenu: '{f_hab}'")
print_test("Bird.habitat() est resté intact", "sky" in b_hab.lower() and "water" not in b_hab.lower(), f"Obtenu: '{b_hab}'")

# ---------------------------------------------------------------------
# TEST 2 : Conformité de FlyingFish (Surcharges)
# ---------------------------------------------------------------------
print("\n--- 2. Comportement de FlyingFish ---")
ff = FlyingFish()

ff_swim = capture_output(ff.swim)
ff_fly = capture_output(ff.fly)
ff_hab = capture_output(ff.habitat)

print_test("FlyingFish.swim() spécifique", ff_swim == "The flying fish is swimming!", f"Obtenu: '{ff_swim}'")
print_test("FlyingFish.fly() spécifique", ff_fly == "The flying fish is soaring!", f"Obtenu: '{ff_fly}'")
print_test("FlyingFish.habitat() combine les deux", ff_hab == "The flying fish lives both in water and the sky!", f"Obtenu: '{ff_hab}'")

# ---------------------------------------------------------------------
# TEST 3 : Typage et hiérarchie (isinstance / issubclass)
# ---------------------------------------------------------------------
print("\n--- 3. Contrôle des types et héritage ---")
print_test("FlyingFish est une instance de Fish", isinstance(ff, Fish))
print_test("FlyingFish est une instance de Bird", isinstance(ff, Bird))
print_test("FlyingFish sous-classe Fish", issubclass(FlyingFish, Fish))
print_test("FlyingFish sous-classe Bird", issubclass(FlyingFish, Bird))

# ---------------------------------------------------------------------
# TEST 4 : Inspection du MRO (Method Resolution Order)
# ---------------------------------------------------------------------
print("\n--- 4. Analyse du MRO (Method Resolution Order) ---")
mro = FlyingFish.__mro__
mro_names = [cls.__name__ for cls in mro]
print(f"MRO détecté : {' -> '.join(mro_names)}")

# Vérifie que les deux parents figurent bien dans la résolution
has_both_parents = "Fish" in mro_names and "Bird" in mro_names
print_test("MRO contient Fish ET Bird", has_both_parents)

# ---------------------------------------------------------------------
# TEST 5 : Appel explicite des méthodes parentes depuis une instance
# ---------------------------------------------------------------------
print("\n--- 5. Accès forcé aux méthodes parentes ---")
try:
    fish_habitat_from_ff = capture_output(Fish.habitat, ff)
    bird_habitat_from_ff = capture_output(Bird.habitat, ff)
    
    print_test("Peut forcer Fish.habitat(flying_fish)", "water" in fish_habitat_from_ff.lower())
    print_test("Peut forcer Bird.habitat(flying_fish)", "sky" in bird_habitat_from_ff.lower())
except Exception as e:
    print_test("Accès explicite aux méthodes parentes", False, str(e))

print("\n" + "=" * 60)