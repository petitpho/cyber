def cesar(message, decalage, chiffrer=True):
    """
    Fonction pour chiffrer ou déchiffrer un message via l'algorithme de César.
    """
    resultat = ""
    # Si on veut déchiffrer, on inverse simplement le décalages
    if not chiffrer:
        decalage = -decalage
    
    for char in message:
        # On ne traite que les lettres (on ignore la ponctuation et les espaces)
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultat += chr((ord(char) - base + decalage) % 26 + base)
        else:
            resultat += char
    
    return resultat

# --- Interface Utilisateur ---
print("=" * 40)
print("   CHIFFREMENT CÉSAR")
print("=" * 40)

print("\nQue voulez-vous faire ?")
print("  1. Chiffrer")
print("  2. Déchiffrer")

# Vérification de la validité du choix de l'utilisateur
choix = input("\nVotre choix (1 ou 2) : ").strip()

while choix not in ("1", "2"):
    choix = input("Choix invalide. Entrez 1 ou 2 : ").strip()

message = input("Entrez votre message : ")

# Gestion d'erreur pour s'assurer que le décalage est bien un nombre entier
while True:
    try:
        decalage = int(input("Entrez la clé (nombre de décalage) : "))
        break
    except ValueError:
        print("Veuillez entrer un nombre entier.")

# Appel de la fonction selon le mode choisi
if choix == "1":
    resultat = cesar(message, decalage, chiffrer=True)
    print(f"\n✅ Message chiffré   : {resultat}")
else:
    resultat = cesar(message, decalage, chiffrer=False)
    print(f"\n✅ Message déchiffré : {resultat}")

print(f"   Clé utilisée     : {decalage}")
print("=" * 40)
