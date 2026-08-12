#!/usr/bin/env python3
import io
import sys
from task_05_dragon import Dragon, SwimMixin, FlyMixin


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
print("  STRESS TEST : MIXINS & DRAGON")
print("=" * 60)

# ---------------------------------------------------------------------
# TEST 1 : Conformité des sorties exactes de Dragon
# ---------------------------------------------------------------------
print("\n--- 1. Vérification des sorties de Dragon ---")
dragon = Dragon()

out_swim = capture_output(dragon.swim)
out_fly = capture_output(dragon.fly)
out_roar = capture_output(dragon.roar)

print_test("Dragon.swim()", out_swim == "The creature swims!", f"Obtenu: '{out_swim}'")
print_test("Dragon.fly()", out_fly == "The creature flies!", f"Obtenu: '{out_fly}'")
print_test("Dragon.roar()", out_roar == "The dragon roars!", f"Obtenu: '{out_roar}'")

# ---------------------------------------------------------------------
# TEST 2 : Strict confinement des Mixins (Étanchéité)
# ---------------------------------------------------------------------
print("\n--- 2. Isolation des Mixins ---")
swim_attrs = dir(SwimMixin)
fly_attrs = dir(FlyMixin)

print_test("SwimMixin possède 'swim'", "swim" in swim_attrs)
print_test("SwimMixin NE possède PAS 'fly'", "fly" not in swim_attrs)
print_test("SwimMixin NE possède PAS 'roar'", "roar" not in swim_attrs)

print_test("FlyMixin possède 'fly'", "fly" in fly_attrs)
print_test("FlyMixin NE possède PAS 'swim'", "swim" not in fly_attrs)
print_test("FlyMixin NE possède PAS 'roar'", "roar" not in fly_attrs)

# ---------------------------------------------------------------------
# TEST 3 : Relation de typage et sous-classement
# ---------------------------------------------------------------------
print("\n--- 3. Polymorphisme et sous-classement ---")
print_test("Dragon est une instance de SwimMixin", isinstance(dragon, SwimMixin))
print_test("Dragon est une instance de FlyMixin", isinstance(dragon, FlyMixin))
print_test("Dragon sous-classe SwimMixin", issubclass(Dragon, SwimMixin))
print_test("Dragon sous-classe FlyMixin", issubclass(Dragon, FlyMixin))

# ---------------------------------------------------------------------
# TEST 4 : MRO (Method Resolution Order)
# ---------------------------------------------------------------------
print("\n--- 4. Inspection de l'arbre d'héritage (MRO) ---")
mro_names = [cls.__name__ for cls in Dragon.__mro__]
print(f"MRO détecté : {' -> '.join(mro_names)}")

print_test("SwimMixin est présent dans le MRO", "SwimMixin" in mro_names)
print_test("FlyMixin est présent dans le MRO", "FlyMixin" in mro_names)

# ---------------------------------------------------------------------
# TEST 5 : Utilisation autonome des Mixins (Reconstitution dynamique)
# ---------------------------------------------------------------------
print("\n--- 5. Test de réutilisabilité des Mixins ---")

class Canard(SwimMixin, FlyMixin):
    pass

coin = Canard()
out_canard_swim = capture_output(coin.swim)
out_canard_fly = capture_output(coin.fly)

print_test("Un autre objet utilisant SwimMixin peut nager", out_canard_swim == "The creature swims!", f"Obtenu: '{out_canard_swim}'")
print_test("Un autre objet utilisant FlyMixin peut voler", out_canard_fly == "The creature flies!", f"Obtenu: '{out_canard_fly}'")

print("\n" + "=" * 60)