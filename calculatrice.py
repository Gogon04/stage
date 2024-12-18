def calculer(expression):
    try:
        nombres = []
        operateurs = []
        
        # Récupérer les entrées utilisateur
        nombres.append(int(input("Premier nombre : ")))
        operateurs.append(input("Premier opérateur (+,-,*,/) : "))
        nombres.append(int(input("Deuxième nombre : ")))
        operateurs.append(input("Deuxième opérateur (+,-,*,/) : "))
        nombres.append(int(input("Troisième nombre : ")))
        
        # Vérifier les opérateurs
        for op in operateurs:
            if op not in '+-*/':
                raise ValueError("Opérateur invalide")
        
        # Calculer le résultat
        resultat = nombres[0]
        for i in range(len(operateurs)):
            if operateurs[i] == '/' and nombres[i + 1] == 0:
                raise ValueError("Division par zéro impossible")
            resultat = eval(f"{resultat}{operateurs[i]}{nombres[i + 1]}")
            
        return resultat
        
    except ValueError as e:
        return f"Erreur : {e}"
    except Exception as e:
        return f"Erreur inattendue : {e}"

# Exécution du programme
if __name__ == "__main__":
    print(f"Résultat : {calculer('')}")