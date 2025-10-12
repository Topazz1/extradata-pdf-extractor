# src/gui/main_window.py

import customtkinter as ctk

from utils.config import DOCUMENT_FIELDS, APP_NAME

class MainWindow(ctk.CTkFrame):

    # la fenêtre principale
    def __init__(self, master=None):
        super().__init__(master, corner_radius=0) 

        # --- Configuration du Frame principal ---
        # Configuration de la grille principale du Frame (main_window)
        self.grid_rowconfigure(0, weight=0) # Pour le titre (ne s'étire pas)
        self.grid_rowconfigure(1, weight=1) # Pour le contenu (s'étire)
        self.grid_columnconfigure(0, weight=1)

        # --- Affichage du titre principal ---
        # (Reste inchangé, mais on le place dans le Frame)
        title_label = ctk.CTkLabel(self, text="Extradata", font=ctk.CTkFont(size=24, weight="bold"))
        # Place le label en haut du Frame (ligne 0)
        title_label.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        # --- Conteneur pour les boutons de catégorie ---
        #On crée un nouveau frame pour contenir les boutons horizontalement 
        self.category_frame = ctk.CTkFrame(self, fg_color="transparent")

        #On place cette categorie juste en dessous du titre.
        self.category_frame.grid(row=1, column=0, padx=20, pady=(0,30), sticky="n")

        # --- Zone de Glisser-Déposer (Drag & Drop) donc ligne 2, a la suite ---
        self.drop_area = ctk.CTkFrame(self, width=400, height=300, fg_color=("gray80", "gray20"))
        
        self.drop_area.grid(row=2, column=0, padx=50, pady=(50, 100), sticky="n") 
        self.drop_area.grid_propagate(False)

        # Texte dans la zone de glisser-déposer
        drop_label = ctk.CTkLabel(self.drop_area, text="Déposez vos fichiers PDF ici", font=ctk.CTkFont(size=18))
        drop_label.grid(row=0, column=0, padx=10, pady=100)

        self.grid_rowconfigure(0, weight=0) # Titre
        self.grid_rowconfigure(1, weight=0) # Nouveau : Category Frame
        self.grid_rowconfigure(2, weight=1) # Nouveau : Zone de drop (qui s'étire)

        # --- Génération des boutons de catégories ---
        categories = DOCUMENT_FIELDS.keys()
        col_index = 0

        for category_name in categories :
            #Créer le bouton : 
            #Premier argument = conteneur parent ; Deuxième argument = le texte du bouton
            button = ctk.CTkButton(self.category_frame, text=category_name)

            #On applique la grille au boutton lui même
            button.grid(row=0, column=col_index, padx=5, pady=5)

            col_index += 1