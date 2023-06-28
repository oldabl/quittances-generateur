# Générateur de quittances de loyer
Le générateur marche sur un terminal Bash.
Prérequis :
- installer les packets suivants : python3 python-is-python3 python3-pip texlive-latex-base texlive-fonts-recommended texlive-lang-french
- avec pip, installer PyYAML et inputimeout

## 1. Configurez vos bien
La configuration de vos différents bien en location se fait dans le fichier *bdd.yml*.
Il doit donc contenir toutes les informations nécessaires pour la génération de quittances :
- propriétaires
- adresses
- locataires
- etc..
Un exemple à suivre se trouve dans le fichier *bdd.yml*.

## 2. Créez vos quittances
Pour generer les quittances du mois en cours, sur un terminal, tapez :
```python
./generer.sh
```

## 3. Changez le mois
Dans le fichier *generateur-quittances.py*, en bas, se trouvent la ligne suivante :
```python
gen = GenerateurQuittances("bdd.yml")
```
Par défaut, les quittances seront générées pour le mois courant.
Si, toutefois, il fallait spécifier un mois différent, alors la ligne suivante peut etre utilisée à la place (par exemple pour janvier 2021) :
```python
gen = GenerateurQuittances("bdd.yml", 01, 2021)
```

## 4. Nettoyez le dossier des fichiers temporaires
PS : le fichier *nettoyer.sh* peut être utilisé de la façon suivante pour supprimer tous les fichiers temporaires créés pendant l'exécution du programme.
Dans un terminal, tapez :
```shell
./nettoyer.sh
```
