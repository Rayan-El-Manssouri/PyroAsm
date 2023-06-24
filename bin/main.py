import sys
import re
from colorama import init, Fore
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtGui import QColor, QPalette, QIcon

# Initialiser colorama
init()

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class Compilateur:
    def __init__(self):
        self.fonctions_autorisees = ["pyrint", "pyrowin"]
        self.est_dans_fonction = False

    def replace_variables(self, code, variables):
        for variable, value in variables.items():
            code = code.replace(variable, str(value))
        return code

    def evaluate_expression(self, expression, variables):
        expression = self.replace_variables(expression, variables)
        return eval(expression)

    def create_window(self, icon_value, title_value, dark_mode):
        # Implémentation de la création de la fenêtre
        pass

    def executer_code(self, code, variables):
        matches = re.findall(r'([a-zA-Z_][a-zA-Z0-9_]*)\((.*?)\)', code)
        for match in matches:
            fonction, value = match
            if fonction in self.fonctions_autorisees:
                if fonction == "pyrint":
                    if not self.est_dans_fonction:
                        value = self.replace_variables(value, variables)
                        print(value)
                elif fonction == "pyrowin":
                    if not self.est_dans_fonction:
                        dark_mode = True
                        if 'dark: false' in value:
                            dark_mode = False

                        if 'icon: ' in value or 'title: ' in value:
                            pairs = value.split(',')
                            icon_value = None
                            title_value = None
                            for pair in pairs:
                                if 'icon: ' in pair:
                                    icon_value = pair.split('icon: ')[1].strip().strip('"')
                                elif 'title: ' in pair:
                                    title_value = pair.split('title: ')[1].strip().strip('"')
                            self.create_window(icon_value, title_value, dark_mode)
            else:
                suggestion = None
                for f in self.fonctions_autorisees:
                    if f.lower() == fonction.lower():
                        suggestion = f
                        break
                print(Fore.RED + "Erreur de frappe :", fonction)
                if suggestion:
                    print("Vouliez-vous dire :", suggestion + "()" + Fore.RESET)

    def compiler(self, arguments):
        variables = {}
        compteur_erreurs = 0

        for argument in arguments:
            with open(argument, "r", encoding="utf-8") as file:
                code = file.read()

                code = code.replace("\n", "")
                functions_to_execute = []
                function_body = ""

                matches = re.findall(r'const\s+(\w+)\s*=\s*(.+)', code)
                for match in matches:
                    variable_name, value = match
                    value = self.evaluate_expression(value, variables)
                    variables[variable_name] = value

                functions_matches = re.findall(r'fp\s+(\w+)\s*\(\s*\)\s*{([^}]*)}', code)
                for match in functions_matches:
                    function_name, function_body = match

                self.est_dans_fonction = True
                self.executer_code(function_body, variables)
                self.est_dans_fonction = False

        if compteur_erreurs == 0:
            print(Fore.GREEN + "La compilation a réussi." + Fore.RESET)
        else:
            print(Fore.RED + "La compilation a échoué." + Fore.RESET)

# Utilisation de la classe Compilateur
arguments = sys.argv[1:]  # Ignorer le premier argument (nom du script)
compilateur = Compilateur()
compilateur.compiler(arguments)
