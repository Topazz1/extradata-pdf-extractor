# test_moteur.py

import sys
import os

# --- Configuration Magique ---
script_dir = os.path.dirname(__file__)
src_dir = os.path.join(script_dir, 'src')
sys.path.append(src_dir)
# -----------------------------

# On peut maintenant importer nos modules !
from core.extractor import extract_text_from_pdf
from core.parser import parse_invoice_data

# --- À CONFIGURER PAR TES SOINS ---
# Mets ici le chemin ABSOLU vers un PDF de facture que tu as sur ton PC
CHEMIN_VERS_TON_PDF_TEST = "src/tests/sample-invoice.pdf" 
# (utilise un 'r' avant les guillemets sur Windows à cause des \ )
# (sur Mac/Linux: "/users/toi/docs/ma_facture_test.pdf")
# -----------------------------------


if not os.path.exists(CHEMIN_VERS_TON_PDF_TEST):
    print("="*50)
    print("ERREUR : Fichier de test non trouvé !")
    print(f"Vérifie le chemin dans 'CHEMIN_VERS_TON_PDF_TEST' : {CHEMIN_VERS_TON_PDF_TEST}")
    print("="*50)
else:
    print(f"--- 1. Lancement de l'extraction sur {CHEMIN_VERS_TON_PDF_TEST} ---")
    texte = extract_text_from_pdf(CHEMIN_VERS_TON_PDF_TEST)
    
    if texte:
        print("--- Extraction Réussie ! (500 premiers caractères) ---")
        print(texte[:500] + "...")
        print("--------------------------------------------------\n")
        
        print("--- 2. Lancement de l'analyse (Parsing) ---")
        donnees = parse_invoice_data(texte)
        
        print("\n--- RÉSULTATS FINAUX DE L'ANALYSE ---")
        import json # Juste pour un affichage plus joli
        print(json.dumps(donnees, indent=2))
        print("---------------------------------------")
        
    else:
        print("--- ÉCHEC de l'extraction. Aucun texte retourné. ---")
        print("Vérifie que ton PDF n'est pas une image scannée.")