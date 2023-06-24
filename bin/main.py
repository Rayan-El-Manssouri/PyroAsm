import sys
import re
from colorama import init, Fore
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtGui import QIcon
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
        # Liste des noms de fonctions autorisées
        self.fonctions_autorisees = ["pyrint", "+", "-", "*", "/", "%", "^=", "const", "pyrowin"]

    def compiler(self, arguments):
        # Afficher le message de début de compilation
        print(Fore.GREEN + "La compilation a commencé." + Fore.RESET)

        # Traiter les arguments
        compteur_erreurs = 0  # Compteur d'erreurs
        for argument in arguments:
            with open(argument, "r", encoding="utf-8") as file:
                
                code = file.read()
                # mettre tous sur une seul ligne
                code = code.replace("\n", "")
                print(code)
                matches = re.findall(r'const\s+(\w+)\s*=\s*(.+)', code)
                variables = {}

                for match in matches:
                    variable_name, value = match
                    value = self.evaluate_expression(value, variables)
                    variables[variable_name] = value

                matches = re.findall(r'([a-zA-Z_][a-zA-Z0-9_]*)\((.+?)\)', code)
                for match in matches:
                    fonction, value = match
                    if fonction in self.fonctions_autorisees:
                        if fonction == "pyrint":
                            if value.startswith('"') and value.endswith('"'):
                                value = value[1:-1]
                            value = self.replace_variables(value, variables)  # Remplacer les variables
                            print(value)
                        if fonction == "pyrowin":
                            dark_mode = True  # Valeur par défaut
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
                        compteur_erreurs += 1


        # Afficher le message de fin de compilation et le nombre d'erreurs
        print(Fore.GREEN + "La compilation est terminée." + Fore.RESET)
        if compteur_erreurs == 0:
            print(Fore.GREEN + "Aucune erreur de frappe détectée." + Fore.RESET)
        else:
            print(Fore.RED + "Nombre total d'erreurs de frappe :", str(compteur_erreurs) + Fore.RESET)


    def evaluate_expression(self, expression, variables):
        return eval(expression, variables)


    def replace_variables(self, value, variables):
        def replace_variable(match):
            variable_name = match.group(1)
            if variable_name in variables:
                return str(variables[variable_name])
            else:
                return match.group(0)

        value = re.sub(r'\$(\w+)', replace_variable, value)
        return value
    
    def create_window(self, Icon, Title, DarkMode):
        if DarkMode == True:
            DarkMode = (12, 12, 13)
        else:
            DarkMode = (255, 255, 255)

        if Icon == None:
            icon = r"C:\\Program Files\\PyroAsm\\assets\\logo.png"
        else:
            icon = Icon

        if Title == None:
            title = "PyRowin"
        else:
            title = Title
        app = QApplication([])
        window = QMainWindow()
        window.setWindowTitle(title)
        window.resize(800, 600)
        title_bar_color = QColor(*DarkMode)
        app.setPalette(QPalette(title_bar_color))
        layout = QVBoxLayout()
        layout.addWidget(Color('white'))
        layout.setContentsMargins(0,0,0,0)
        widget = QWidget()
        widget.setLayout(layout)
        window.setCentralWidget(widget)
        # definir une icon
        icon = QIcon(icon)
        window.setWindowIcon(icon)
        window.show()
        sys.exit(app.exec())

# Utilisation de la classe Compilateur
arguments = sys.argv[1:]  # Ignorer le premier argument (nom du script)
compilateur = Compilateur()
compilateur.compiler(arguments)
