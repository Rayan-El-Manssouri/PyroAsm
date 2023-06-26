# Documentation Pyro Asm v0.1.0

Bienvenue dans la documentation de Pyro Asm ! Cette documentation vise à vous aider à comprendre et à utiliser le langage Pyro Asm.

## Déclaration de fonctions

Pour déclarer une fonction dans Pyro Asm, utilisez la syntaxe suivante :

```white
fp test{
    pyrint("test")
}
```


Dans cet exemple, nous déclarons une fonction nommée "test" qui affiche le mot "test" à l'écran en utilisant la commande `pyrint`. Vous pouvez remplacer le code à l'intérieur des accolades par le contenu de votre fonction.

## Exécution d'une fonction

Une fois que vous avez déclaré une fonction, vous pouvez l'exécuter en appelant son nom suivi de parenthèses vides, comme ceci :

```white
test()
```


L'appel de cette fonction affichera le mot "test" à l'écran.

## Exécution du code Pyro Asm

Pour exécuter un fichier contenant du code Pyro Asm, utilisez la commande suivante dans votre terminal :

```white
pyroasm -r NomDuFichier.pa
```


Assurez-vous de remplacer "NomDuFichier.pa" par le nom réel de votre fichier contenant le code Pyro Asm. Cette commande exécutera le code contenu dans le fichier et produira le résultat correspondant.

## Création d'une fenêtre

Pyro Asm permet également de créer des fenêtres graphiques. Pour créer une fenêtre, utilisez la fonction `pyrowin` avec le nom souhaité pour votre fenêtre, comme ceci :


```white
fp main{
    pyrowin(close_.png, Hello World)
}

main()
```


Si vous souhaiter avoir la barre des titres noir alors ne mettre aucuns de 3er arguements paramètres à la fonction `pyrowin`.
```white
fp main{
    pyrowin(close_.png, Hello World)
}

main()
```


Cette commande créera une fenêtre avec le nom spécifié et l'icon / mode fond.


* Note : Vous pouvez également utiliser la fonction `pyrowin` sans paramètre pour créer une fenêtre sans nom. Cependant, il est recommandé d'utiliser un nom pour votre fenêtre afin de pouvoir la fermer plus tard.
- Actuellement, il est nécessaire de mettre tous les éléments dans une fonction déclarée dans la fonction principale (main ou autre selon vôtre choix) pour que cela fonctionne correctement.

N'hésitez pas à explorer davantage la documentation de Pyro Asm pour découvrir d'autres fonctionnalités et options disponibles.

