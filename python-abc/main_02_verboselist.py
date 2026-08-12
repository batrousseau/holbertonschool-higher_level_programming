#!/usr/bin/env python3
from task_02_verboselist import VerboseList

print("=== DEBUT DU TEST DE VERBOSELIST ===")

# ---------------------------------------------------------
# TEST 1 : Append basique
# ---------------------------------------------------------
print("\n--- 1. Test append(30) ---")
vl = VerboseList([10, 20])
vl.append(30)

if len(vl) == 3 and vl[-1] == 30:
    print("  ✅ [SUCCÈS] L'élément a bien été ajouté à la liste.")
else:
    print("  ❌ [ÉCHEC] L'élément n'a pas été ajouté correctement.")

# ---------------------------------------------------------
# TEST 2 : Extend avec un itérable sans taille fixe (Générateur)
# ---------------------------------------------------------
print("\n--- 2. Test extend avec un générateur (ex: x for x in range(3)) ---")
try:
    vl.extend(x for x in range(3))
    print("  ✅ [SUCCÈS] L'extend a fonctionné sans planter.")
except TypeError as e:
    if "len()" in str(e) or "has no len" in str(e):
        print("  ❌ [ÉCHEC] Ton code a crashé parce qu'il cherche la taille len() du générateur.")
    else:
        print(f"  ❌ [ÉCHEC] Erreur inattendue : {e}")

# ---------------------------------------------------------
# TEST 3 : Extend avec un objet non-itérable (ex: 42)
# ---------------------------------------------------------
print("\n--- 3. Test extend(42) [Doit lever une TypeError] ---")
try:
    vl.extend(42)
    print("  ❌ [ÉCHEC] extend(42) aurait dû lever une TypeError, mais rien ne s'est passé !")
except TypeError:
    print("  ✅ [SUCCÈS] La TypeError a bien été levée pour un non-itérable.")
except Exception as e:
    print(f"  ❌ [ÉCHEC] Mauvaise exception levée : {type(e).__name__}")

# ---------------------------------------------------------
# TEST 4 : Pop et retour de valeur
# ---------------------------------------------------------
print("\n--- 4. Test de la valeur de retour de pop() ---")
vl_pop = VerboseList([100, 200, 300])
valeur_retournee = vl_pop.pop()

if valeur_retournee == 300:
    print(f"  ✅ [SUCCÈS] pop() a renvoyé la bonne valeur (300).")
elif valeur_retournee is None:
    print("  ❌ [ÉCHEC] pop() a renvoyé None au lieu de la valeur supprimée (300).")
else:
    print(f"  ❌ [ÉCHEC] pop() a renvoyé {valeur_retournee} au lieu de 300.")

# ---------------------------------------------------------
# TEST 5 : Vérification de la méthode native .index()
# ---------------------------------------------------------
print("\n--- 5. Test de résistance de la méthode native vl.index() ---")
try:
    # On fait un pop d'abord pour voir si self.index = index a cassé la méthode
    vl_test = VerboseList(["a", "b", "c"])
    vl_test.pop(0) 
    
    # On teste ensuite si .index() fonctionne toujours
    pos = vl_test.index("c")
    print(f"  ✅ [SUCCÈS] La méthode vl.index() fonctionne toujours correctement.")
except TypeError:
    print("  ❌ [ÉCHEC] La méthode vl.index() a été écrasée par un entier (attribut `self.index`) !")
except Exception as e:
    print(f"  ❌ [ÉCHEC] Erreur inattendue : {e}")

print("\n=== FIN DU TEST ===")