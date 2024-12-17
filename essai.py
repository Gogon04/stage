# Demande à l'utilisateur d'entrer deux nombres et un opérateur
a = int(input("Entrer un premier nombre A: "))
b = int(input("Entrer un second nombre B: "))
c = input("Entrer votre opérateur (+, -, *, /): ")

# Initialisation de la variable d
d = 0

# Vérification de l'opérateur et calcul
if c == '+':
    d = a + b
elif c == '-':
    d = a - b
elif c == '*':
    d = a * b
elif c == '/':
    if b != 0:  # Vérification pour éviter la division par zéro
        d = a / b
    else:
        print("Erreur: Division par zéro.")
        d = None
else:
    print("Erreur: Opérateur non valide.")
    d = None

# Affichage du résultat
if d is not None:
    print("Le résultat est:", d)