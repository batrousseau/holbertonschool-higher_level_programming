#!/usr/bin/python3
"""
Fichier de test avancé pour valider roman_to_int
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

# Liste des cas de test : (valeur_injectee, valeur_attendue_int, description)
test_cases = [
    # --- CAS DE BASE DU PROMPT ---
    ("X", 10, "Cas simple"),
    ("VII", 7, "Cas simple"),
    ("LXXXVII", 87, "Nombre moyen complexe"),
    ("DCCVII", 707, "Grand nombre classique"),
    
    # --- CAS LIMITES : TOUTES LES NOTATIONS SOUSTRACTIVES (Pièges du i + 1) ---
    ("IV", 4, "Soustraction : 1 avant 5"),
    ("IX", 9, "Soustraction : 1 avant 10"),
    ("XL", 40, "Soustraction : 10 avant 50"),
    ("XC", 90, "Soustraction : 10 avant 100"),
    ("CD", 400, "Soustraction : 100 avant 500"),
    ("CM", 900, "Soustraction : 100 avant 1000"),
    
    # --- CAS LIMITES : COMBINAISONS IMPRÉVISIBLES ---
    ("MCMXCIX", 1999, "Multiples soustractions successives (900 + 90 + 9)"),
    ("MMXCDV", 2445, "Soustraction CD isolée en milieu de chaîne"),
    ("XIV", 14, "Soustraction finale après une grande valeur"),
    
    # --- CAS LIMITES : BORNES EXTENSIVES ---
    ("I", 1, "Le plus petit chiffre romain possible"),
    ("MMMCMXCIX", 3999, "Le plus grand nombre standard (Fin de boucle stricte)"),
    ("MMMDCCCLXXXVIII", 3888, "Le nombre romain le plus long (15 caractères, sature la mémoire)"),
    
    # --- CAS LIMITES : PROGRAMMATION DÉFENSIVE (Devrait renvoyer 0 sans crasher) ---
    ("", 0, "Chaîne vide"),
    (None, 0, "Valeur de type None"),
    (12, 0, "Entier injecté à la place d'une string"),
    (["X", "I"], 0, "Liste injectée à la place d'une string"),
]

# En-tête d'affichage propre
print(f"{'ENTRÉE':<18} | {'ATTENDU':<7} | {'OBTENU':<7} | {'RÉSULTAT'}")
print("-" * 65)

# Lancement de la suite de tests
for roman, expected, desc in test_cases:
    # Formatage propre du texte d'entrée selon son type pour éviter les bugs d'affichage
    display_input = f'"{roman}"' if isinstance(roman, str) else str(roman)
    
    try:
        result = roman_to_int(roman)
        
        if result == expected:
            status = "✅ OK"
        else:
            status = f"❌ ERREUR (Reçu {result} au lieu de {expected})"
            
        print(f"{display_input:<18} | {expected:<7} | {result:<7} | {status} — [{desc}]")
        
    except Exception as e:
        # Si ton code crash (ex: IndexError), le script ne s'arrête pas et te montre la ligne coupable
        print(f"{display_input:<18} | {expected:<7} | 💥 CRASH  | ❌ Déclenché : {type(e).__name__} — [{desc}]")