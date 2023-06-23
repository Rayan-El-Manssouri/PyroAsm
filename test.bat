@echo off

set "ligne=pyrint("Premier programme de compilation et d'exécution de code PyAsm" "

for /F "tokens=2 delims=()" %%a in ("%ligne%") do set "contenu=%%a"

echo %contenu%
