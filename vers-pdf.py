# import os
# variables = ""
# variables += "\\def\\jourdepaiement{10} "
# variables += "\\def\\loyerchiffres{350} "
# variables += "\\def\\loyerlettres{trois cent cinquante} "
# variables += "\\def\\charges{0} "
# variables += "\\def\\economisenergies{0} "

# variables += "\\def\\nomlocataire{Mr Tony Haddock} "
# variables += "\\def\\adresselocataire{16 rue des Marins d'Eau Douce} "
# variables += "\\def\\villelocataire{12345 Sabords} "
# variables += "\\def\\adresselocation{16 rue des Duponts, Appartement 4} "
# variables += "\\def\\villelocation{54321 Jumeaux} "
# variables += "\\def\\lieudocument{Paris} "
# variables += "\\def\\totalpaiement{350} "
# variables += "\\def\\datepaiement{10/02/2022} "
# os.system(" pdflatex \""+variables+" \input{modele-quittance-appt-meuble-vide.tex}\" ")

import GenerateurQuittances
generateur = GenerateurQuittances("bdd.yml")
