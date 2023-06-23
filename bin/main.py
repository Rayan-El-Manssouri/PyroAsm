import sys
import re
from colorama import init, Fore

# Initialiser colorama
init()

class Compilateur:
    def __init__(self):
        # Liste des noms de fonctions autorisées
        self.fonctions_autorisees = ["pyrint"]

    def compiler(self, arguments):
        # Afficher le message de début de compilation
        print(Fore.GREEN + "La compilation a commencé." + Fore.RESET)

        # Traiter les arguments
        compteur_erreurs = 0  # Compteur d'erreurs
        for argument in arguments:
            with open(argument, "r") as file:
                code = file.read()
                matches = re.findall(r'([a-zA-Z_][a-zA-Z0-9_]*)\((.+?)\)', code)
                for match in matches:
                    fonction, value = match
                    if fonction in self.fonctions_autorisees:
                        value = value.strip('"')
                        print(value)
                    else:
                        suggestion = None
                        for f in self.fonctions_autorisees:
                            if f.lower() == fonction.lower():
                                suggestion = f
                                break
                        print(Fore.RED + "Erreur de frappe :", fonction)
                        if suggestion:
                            print("Vouliez-vous dire :", suggestion + "()" + Fore.RESET)
                        compteur_erreurs += 1  # Incrémenter le compteur d'erreurs

        # Afficher le message de fin de compilation et le nombre d'erreurs
        print(Fore.GREEN + "La compilation est terminée." + Fore.RESET)
        if compteur_erreurs == 0:
            print(Fore.GREEN + "Aucune erreur de frappe détectée." + Fore.RESET)
        else:
            print(Fore.RED + "Nombre total d'erreurs de frappe :", str(compteur_erreurs) + Fore.RESET)

# Utilisation de la classe Compilateur
arguments = sys.argv[1:]  # Ignorer le premier argument (nom du script)
compilateur = Compilateur()
compilateur.compiler(arguments)
