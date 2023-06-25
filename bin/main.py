import sys
import re
from colorama import init, Fore
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
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
        # Liste des noms de fonctions autorisées
        self.fonctions_autorisees = ["pyrint", "+", "-", "*", "/", "%", "^=", "const", "pyrowin", "fp"]
        self.fonctions_declarees = {}
        self.fonction_executant = None

    def compiler(self, arguments):
        # Afficher le message de début de compilation
        print(Fore.GREEN + "La compilation a commencé." + Fore.RESET)
        # Traiter les arguments
        compteur_erreurs = 0  # Compteur d'erreurs
        for argument in arguments:
            code_complet = ""
            with open(argument, "r", encoding="utf-8") as file:
                code = file.read()
                code = code.replace("\n", "")
   
                code_complet += code
                self.process_function_declarations(code_complet)
                self.process_function_calls(code_complet)
                
        # Afficher le message de fin de compilation et le nombre d'erreurs
        print(Fore.GREEN + "La compilation est terminée." + Fore.RESET)
        if compteur_erreurs == 0:
            print(Fore.GREEN + "Aucune erreur de frappe détectée." + Fore.RESET)
        else:
            print(Fore.RED + "Nombre total d'erreurs de frappe :", str(compteur_erreurs) + Fore.RESET)


    def process_const_declarations(self, code):
        matches = re.findall(r'const\s+(\w+)\s*=\s*(.+)', code)
        variables = {}
        for match in matches:
            variable_name, value = match
            value = self.evaluate_expression(value, variables)
            variables[variable_name] = value

        return variables
    
    def process_function_declarations(self, code):
        matches = re.findall(r'fp\s+(\w+)\s*\(\)\s*\{([^}]+)\}', code)
        for match in matches:
            fonction_name, fonction_code = match
            self.fonctions_declarees[fonction_name] = fonction_code
        
    def process_function_calls(self, code):
        pattern = r'(\w+)\s*\(\s*\)'
        matches = re.findall(pattern, code)
        function_calls = []  # Liste pour stocker les appels de fonctions
        for match in matches:
            function_name = match
            function_calls.append(function_name)  # Ajouter l'appel de fonction à la liste

        # Exécuter les appels de fonctions
        for function_name in function_calls:
            self.executer_fonction(function_name)

        

    def executer_fonction(self, fonction_name):
        # regarder dans liste
        if fonction_name in self.fonctions_declarees:
            # récupe le code de la fonction
            fonction_code = self.fonctions_declarees[fonction_name]

            # Sauvegarder la fonction en cours d'exécution
            self.fonction_executant = fonction_name

            # exécuter le code de la fonction
            self.executer_code(code=fonction_code)

            # Réinitialiser le drapeau de la fonction en cours d'exécution
            self.fonction_executant = None
            
    def executer_code(self, code):
        matches = re.findall(r'pyrint\s*\(\s*(.+)\s*\)', code)
        for match in matches:
            value = match.replace('"', '')
            # Exécuter uniquement si la fonction en cours d'exécution correspond
            if self.fonction_executant is None or self.fonction_executant == "__main__":
                print(value)

        matches = re.findall(r'pyrowin\s*\(\s*(.+)\s*\)', code)
        for match in matches:
            value = match.replace('"', '')
            # Exécuter uniquement si la fonction en cours d'exécution correspond
            if self.fonction_executant is None or self.fonction_executant == "__main__":
                self.create_window(Icon=None, Title=value, DarkMode=True)
             
            
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
        layout.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(layout)
        window.setCentralWidget(widget)
        # Définir une icône
        icon = QIcon(icon)
        window.setWindowIcon(icon)
        window.show()
        sys.exit(app.exec())

# Utilisation de la classe Compilateur
arguments = sys.argv[1:]  # Ignorer le premier argument (nom du script)
compilateur = Compilateur()
compilateur.compiler(arguments)
