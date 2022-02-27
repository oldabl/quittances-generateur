import os
variables = ""
variables += "\\def\\nommois{février} "
variables += "\\def\\numeromois{02} "
variables += "\\def\\annee{2022} "
variables += "\\def\\jourdepaiement{10} "
variables += "\\def\\loyerchiffres{350} "
variables += "\\def\\loyerlettres{trois cent cinquante} "
variables += "\\def\\charges{0} "
variables += "\\def\\economisenergies{0} "
variables += "\\def\\nomproprio{Mr Tintin Journaliste} "
variables += "\\def\\adresseproprio{Ici, Batiment La Bas} "
variables += "\\def\\villeproprio{81367 La Fourche} "
variables += "\\def\\nomlocataire{Mr Tony Haddock} "
variables += "\\def\\adresselocataire{16 rue des Marins d'Eau Douce} "
variables += "\\def\\villelocataire{12345 Sabords} "
variables += "\\def\\adresselocation{16 rue des Duponts, Appartement 4} "
variables += "\\def\\villelocation{54321 Jumeaux} "
variables += "\\def\\lieudocument{Paris} "
variables += "\\def\\debutmois{01/02/2022} "
variables += "\\def\\finmois{28/02/2022} "
variables += "\\def\\totalpaiement{350} "
variables += "\\def\\datepaiement{10/02/2022} "
os.system(" pdflatex \""+variables+" \input{modele-appt-meuble.tex}\" ")

# from pdflatex import PDFLaTeX

# pdfl = PDFLaTeX.from_texfile('modele-appt-meuble.tex')
# pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
