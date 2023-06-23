@echo off
setlocal
chcp 65001 > nul
set "scriptPath=C:\Program Files\PyroAsm\bin\main.py"

rem Vérifier si l'option "--version" est présente
if "%~1"=="--version" (
    echo Version 1.0
    exit /b
)

rem Vérifier si l'option "--help" est présente
if "%~1"=="--help" (
    echo Liste des options:
    echo --version: Affiche la version du compilateur
    echo --help: Affiche la liste des options
    echo -r: Compile le fichier spécifié
)

rem Vérifier si l'option "-r" est présente avec un fichier spécifié
if "%~1"=="-r" (
    if not "%~2"=="" (
        rem Exécuter la commande pour compiler le fichier spécifié
        python "%scriptPath%" "%~2"
        exit /b
    )
)

rem Si aucune option n'est fournie, exécuter le script Python
echo Compilateur PyroASM 1.0