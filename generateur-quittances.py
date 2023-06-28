import yaml, os, datetime, calendar

# Tableau qui fait la correspondance entre les numéro de mois et leur nom en français
mois_francais = { "01": "janvier",
                  "02": "février",
                  "03": "mars",
                  "04": "avril",
                  "05": "mai",
                  "06": "juin",
                  "07": "juillet",
                  "08": "août",
                  "09": "septembre",
                  "10": "octobre",
                  "11": "novembre",
                  "12": "décembre"}

#
# Classe qui permet de générer des quittances en PDF à partir d'un fichier YAML
#
class GenerateurQuittances:
  def __init__(self, fichier_bdd, mois = datetime.datetime.now().strftime("%m"), annee = datetime.datetime.now().strftime("%Y"), premierjour = 1):
    self.fichier_bdd = fichier_bdd
    self.mois = str(mois).zfill(2)
    self.annee = str(annee)
    self.premierjour = str(premierjour)
  def creerQuittances(self):
    self.bddVersQuittances()

  # Crée une chaine de variables avec les informations du propriétaire
  def rapporterVariablesProprioPourLatex(self, bdd):
    variables = ""
    variables += " \\def\\nomproprio{"+str(bdd['proprietaire']['nom'])+"} "
    variables += " \\def\\adresseproprio{"+str(bdd['proprietaire']['adresse'])+"} "
    variables += " \\def\\villeproprio{"+str(bdd['proprietaire']['code_postal']) +" "+ str(bdd['proprietaire']['ville'])+"} "
    variables += " \\def\\lieudocument{"+str(bdd['proprietaire']['ville'])+"} "
    return variables

  # Crée une chaine de variables avec les informations du locataire du lot
  def rapporterVariablesInfoLocatairePourLatex(self, lot):
    variables = ""
    variables += " \\def\\lotlocation{"+str(lot['numero'])+"} "
    variables += " \\def\\nomlocataire{"+str(lot['nom_locataire'])+"} "
    variables += " \\def\\adresselocataire{"+str(lot['adresse_locataire'])+"} "
    variables += " \\def\\villelocataire{"+str(lot['ville_locataire'])+"} "
    variables += " \\def\\typedelot{"+str(lot['type_lot'])+"} "
    variables += " \\def\\loyerchiffres{"+str(lot['montant_loyer'])+"} "
    variables += " \\def\\charges{"+str(lot['montant_charges'])+"} "
    variables += " \\def\\loyerccchiffres{"+str(lot['montant_total_chiffres'])+"} "
    variables += " \\def\\loyercclettres{"+str(lot['montant_total_lettres'])+"} "
    variables += " \\def\\montantrecuchiffres{"+str(lot['montant_recu_chiffres'])+"} "
    variables += " \\def\\montantreculettres{"+str(lot['montant_recu_lettres'])+"} "
    variables += " \\def\\montantimpayechiffres{"+str(round(float(lot['montant_total_chiffres'])-float(lot['montant_recu_chiffres']), 2))+"} "
    variables += " \\def\\datepaiement{"+str(lot['jour_paiement_mois']).zfill(2)+"/"+self.mois+"/"+self.annee+"} "
    return variables

  # Crée une chaine de variables avec les informations de l'adresse de la location
  def rapporterVariablesAdresseLocationPourLatex(self, adresse):
    variables = ""
    variables += " \\def\\adresselocation{"+str(adresse.split(',')[0])+"} "
    variables += " \\def\\villelocation{"+str(adresse.split(',')[1])+"} "
    return variables

  # Crée une chaine de variables avec les informations sur les différentes dates nécessaires
  def creerVariablesDatePourLatex(self):
    variables = ""
    date = datetime.datetime.strptime(self.annee+"-"+self.mois+"-"+str(self.premierjour).zfill(2), "%Y-%m-%d")
    jour_fin_mois = str(calendar.monthrange(int(self.annee), int(self.mois))[1])
    variables += " \\def\\nommois{"+str(mois_francais[date.strftime("%m")])+"} "
    variables += " \\def\\numeromois{"+str(date.strftime("%m"))+"} "
    variables += " \\def\\annee{"+str(self.annee)+"} "
    variables += " \\def\\debutmois{"+str(date.strftime("%d/%m/%Y"))+"} "
    variables += " \\def\\finmois{"+str(date.strftime(jour_fin_mois+"/%m/%Y"))+"} "
    return variables

  # Retourne le nom de famille du locataire (dernier mot du nom complet)
  def rapporterNomLocataire(self, lot):
    return lot['nom_locataire'].split(" ")[-1]

  # Génère les quittances en PDF depuis la base de donnée YAML
  def bddVersQuittances(self):
    with open(self.fichier_bdd) as f:
      bdd = yaml.load(f, Loader=yaml.FullLoader)
      toutes_variables_necessaires = ""
      toutes_variables_necessaires += self.rapporterVariablesProprioPourLatex(bdd)
      toutes_variables_necessaires += self.creerVariablesDatePourLatex()
      for adresse_info in bdd['adresses']:
        toutes_variables_necessaires += self.rapporterVariablesAdresseLocationPourLatex(adresse_info['adresse'])
        for lot in adresse_info['lots']:
          toutes_variables_necessaires += self.rapporterVariablesInfoLocatairePourLatex(lot)
          toutes_variables_necessaires = " ".join(toutes_variables_necessaires.split())
          nom_famille_locataire = self.rapporterNomLocataire(lot)
          recuouquittance = "quittance"
          recuouquittancetexte = "Quittance"
          if lot['montant_total_chiffres'] != lot['montant_recu_chiffres'] or lot['montant_total_lettres'] != lot['montant_recu_lettres']:
            recuouquittance = "reculoyer"
            recuouquittancetexte = "Recu"
          nom_fichier = recuouquittancetexte+" loyer "+nom_famille_locataire+" "+self.annee+"."+self.mois
          os.system(" pdflatex -jobname '"+nom_fichier+"' -output-format pdf \""+toutes_variables_necessaires+" \input{modele-"+recuouquittance+"-"+lot['type_lot']+".tex}\" > "+nom_fichier+".log")
          print(recuouquittancetexte+" de loyer pour "+lot['nom_locataire']+" générée dans '"+nom_fichier+".pdf'")
          if 'dossier_disque' in bdd['proprietaire']:
            destination = bdd['proprietaire']['dossier_disque']+"/Bien - Immeuble "+adresse_info['adresse_courte']+"/Location/"+lot['numero']+"/Locataire courant - "+lot['nom_locataire']
            text = input("Copier dans '"+destination+"' ? (y/N)'")
            if text in ('Y', 'y', 'yes', 'yeS', 'yEs', 'yES', 'Yes', 'YeS', 'YEs', 'YES'):
              os.system("cp '"+nom_fichier+".pdf' '"+destination+"'")
              print("-> copiée dans : "+destination)


# Appelle le générateur de quittances et crée les quittances
gen = GenerateurQuittances("bdd.yml")
gen.creerQuittances()
