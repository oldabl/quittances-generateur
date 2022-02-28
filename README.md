# quittances-generateur
Requis :
- installer pdflatex sur son environnement
- installer PyYAML avec pip

python generateur-quittances.py``

Dans le fichier generateur-quittances.py, en bas, se trouvent les lignes suivantes :
gen = GenerateurQuittances("bdd.yml")

Par défaut, les quittances seront générées pour le mois courant. Si toute fois il fallait spécifier un mois différent, alors la ligne suivante peut etre utilisée (par exemple pour janvier 2021) :
gen = GenerateurQuittances("bdd.yml", 01, 2021)

Le fichier bdd.yml doit contenir toutes les informations de la situation : propriétaires, adresses, locataires, etc..
Un exemple à suivre se trouve dans le fichier bdd.yml.
