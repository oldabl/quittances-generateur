import yaml, os, datetime, calendar

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

class GenerateurQuittances:
  def __init__(self, fichier_bdd, mois = datetime.datetime.now().strftime("%m"), annee = datetime.datetime.now().strftime("%Y")):
    self.fichier_bdd = fichier_bdd
    self.mois = mois
    self.annee = annee
  def creerQuittances(self):
    self.bddVersQuittances()
  def rapporterVariablesProprioPourLatex(self, bdd):
    variables = ""
    variables += " \\def\\nomproprio{"+bdd['proprietaire']['nom']+"} "
    variables += " \\def\\adresseproprio{"+bdd['proprietaire']['adresse']+"} "
    variables += " \\def\\villeproprio{"+bdd['proprietaire']['code_postal'] +" "+ bdd['proprietaire']['ville']+"} "
    variables += " \\def\\lieudocument{"+bdd['proprietaire']['ville']+"} "
    return variables
  def rapporterVariablesInfoLocatairePourLatex(self, lot):
    variables = ""
    variables += " \\def\\loyerchiffres{"+lot['montant_loyer']+"} "
    variables += " \\def\\charges{"+lot['montant_charges']+"} "
    if "montant_economies_energie" in lot:
      variables += " \\def\\economisenergies{"+lot['montant_economies_energie']+"} "
    else:
      variables += " \\def\\economisenergies{0} "
    variables += " \\def\\nomlocataire{"+lot['nom_locataire']+"} "
    variables += " \\def\\adresselocataire{"+lot['adresse_locataire']+"} "
    variables += " \\def\\villelocataire{"+lot['ville_locataire']+"} "
    variables += " \\def\\lotlocation{"+lot['numero']+"} "
    variables += " \\def\\totalpaiementchiffres{"+lot['montant_total_chiffres']+"} "
    variables += " \\def\\totalpaiementlettres{"+lot['montant_total_lettres']+"} "
    variables += " \\def\\datepaiement{"+lot['jour_paiement_mois']+"/"+self.mois+"/"+self.annee+"} "
    return variables
  def rapporterVariablesAdresseLocationPourLatex(self, adresse):
    variables = ""
    variables += " \\def\\adresselocation{"+adresse.split(',')[0]+"} "
    variables += " \\def\\villelocation{"+adresse.split(',')[1]+"} "
    return variables
  def creerVariablesDatePourLatex(self):
    variables = ""
    date = datetime.datetime.strptime(self.annee+"-"+self.mois+"-01", "%Y-%m-%d")
    jour_fin_mois = str(calendar.monthrange(int(self.annee), int(self.mois))[1])
    variables += " \\def\\nommois{"+mois_francais[date.strftime("%m")]+"} "
    variables += " \\def\\numeromois{"+date.strftime("%m")+"} "
    variables += " \\def\\annee{"+datetime.datetime.now().strftime("%Y")+"} "
    variables += " \\def\\debutmois{"+date.strftime("%d/%m/%Y")+"} "
    variables += " \\def\\finmois{"+date.strftime(jour_fin_mois+"/%m/%Y")+"} "
    return variables
  def rapporterNomLocataire(self, lot):
    return lot['nom_locataire'].split(" ")[-1]
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
          nom_fichier = "Quittance loyer "+nom_famille_locataire+" "+self.annee+"."+self.mois
          os.system(" pdflatex -jobname '"+nom_fichier+"' -output-format pdf \""+toutes_variables_necessaires+" \input{modele-quittance-"+lot['type_lot']+".tex}\" ")
      

gen = GenerateurQuittances("bdd.yml")
gen.creerQuittances()
