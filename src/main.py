# src/main.py

import customtkinter as ctk
import sys
import os

# Ajout du répertoire parent 'src' au chemin (path)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import de la classe de la fenêtre principale
from gui.main_window import MainWindow 

# Configuration de base de customtkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    # 1. Crée la fenêtre principale (root window)
    app = ctk.CTk() 
    
    # 2. Configuration de la fenêtre
    app.title("Extradata - PDF Extractor")
    app.geometry("800x600")
    app.resizable(False, False)
    
    # *** ÉLÉMENTS CRUCIAUX POUR QUE LE CONTENU S'ÉTEND ***
    
    # 3. On configure la grille de la fenêtre 'app' pour que la ligne et la colonne 0 
    #    (où sera notre 'main_view') aient un 'poids' (weight) de 1. 
    #    Cela signifie qu'elles s'étirent et prennent tout l'espace disponible.
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    # 4. On crée et affiche notre contenu (le CTkFrame MainWindow)
    main_view = MainWindow(master=app)
    
    # 5. On place le Frame 'main_view' dans la fenêtre 'app'. 
    #    Le sticky="nsew" (North, South, East, West) force le Frame à coller 
    #    aux quatre côtés de la cellule de la grille (qui s'étire grâce au weight=1).
    main_view.grid(row=0, column=0, sticky="nsew")

    # 6. Lance la boucle principale
    app.mainloop()