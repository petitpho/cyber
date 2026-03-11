import hashlib

# 1. On choisit l'algorithme et on encode la chaîne en bytes
texte = "texte à encoder"
texte_en_bytes = texte.encode()

# 2. On crée l'objet de hashage
objet_hash = hashlib.sha256(texte_en_bytes)

# 3. On récupère le résultat en hexadécimal
resultat = objet_hash.hexdigest()

print(f"Le hash est : {resultat}")