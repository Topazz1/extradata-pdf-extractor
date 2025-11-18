#src/utils/config.py

#Configuration générale de l'application
APP_NAME = "Extradata"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

#Configuration thèmes interface CustomTkinter
COLOR_THEME = "blue"
APPEARANCE_MODE = "System"

#Définition des champs a extraire (utilisés pour le parceur)
DOCUMENT_FIELDS = {
    "Factures" : [
        "Montant Total",
        "Date de Facture",
        "Numéro de Facture",
        "Nom du Client",
        "Adresse"
    ],
    #Mettre les uatres documents ainsi de suite.
    "CVs" : [], #Sera completé plus tard
    "Autres documents": [] #Sera complété plus tard
}