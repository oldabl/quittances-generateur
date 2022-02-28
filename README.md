# Generateur de quittances de loyer
Prérequis :
- installer pdflatex et python sur son environnement
- installer PyYAML avec pip

Sur un terminal :
```python
python generateur-quittances.py
```

Dans le fichier *generateur-quittances.py*, en bas, se trouvent la ligne suivante :
```python
gen = GenerateurQuittances("bdd.yml")
```

Par défaut, les quittances seront générées pour le mois courant. Si toute fois il fallait spécifier un mois différent, alors la ligne suivante peut etre utilisée à la place (par exemple pour janvier 2021) :
```python
gen = GenerateurQuittances("bdd.yml", 01, 2021)

```
Le fichier *bdd.yml* doit contenir toutes les informations de la situation : propriétaires, adresses, locataires, etc..
Un exemple à suivre se trouve dans le fichier *bdd.yml*.

PS : le fichier *nettoyer.sh* peut être utilisé de la façon suivante pour supprimer tous les fichiers temporaires créés pendant l'exécution du programme :
```shell
./nettoyer.sh
```
