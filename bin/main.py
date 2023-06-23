import sys

# Récupérer les arguments passés au script
arguments = sys.argv[1:]  # Ignorer le premier argument (nom du script)

# Traiter les arguments
for argument in arguments:
    print("Argument:", argument)
    with open(argument, "r") as file:
        print(file.read())
