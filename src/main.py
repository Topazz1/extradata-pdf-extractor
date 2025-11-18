# src/main.py

import customtkinter as ctk
import sys
import os

# --- 1. CONFIGURATION DU CHEMIN (CRUCIAL) ---
# Ceci permet d'importer les modules des dossiers 'gui', 'core', et 'utils'.
# Sans cela, les imports échouent.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# --- 2. IMPORTS DES MODULES ET CONFIGURATIONS ---
from gui.main_window import MainWindow 
from utils.config import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT, COLOR_THEME, APPEARANCE_MODE


if __name__ == "__main__":
    
    # 3. PRÉPARATION DE L'ENVIRONNEMENT CTk
    ctk.set_appearance_mode(APPEARANCE_MODE)
    ctk.set_default_color_theme(COLOR_THEME)

    # 4. CRÉATION DE LA FENÊTRE PRINCIPALE (ROOT)
    app = ctk.CTk() 
    
    # 5. CONFIGURATION DE LA FENÊTRE
    app.title(f"{APP_NAME} - PDF Extractor")
    app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    app.resizable(False, False)
    
    # 6. CONFIGURATION DE LA GRILLE POUR REMPLIR L'ESPACE (Anti-bug de "fenêtre vide")
    # Indique à Tkinter que le Frame (MainWindow) doit s'étirer dans la ligne et colonne 0.
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    # 7. CRÉATION ET AFFICHAGE DU FRAME PRINCIPAL
    # MainWindow est un Frame qui prend toute la place de la fenêtre 'app'.
    main_view = MainWindow(master=app)
    # sticky="nsew" force le Frame à coller aux quatre côtés de la grille.
    main_view.grid(row=0, column=0, sticky="nsew")

    # 8. LANCEMENT DE LA BOUCLE D'ÉVÉNEMENTS
    app.mainloop()