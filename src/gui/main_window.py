# src/gui/main_window.py

import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD

from utils.config import DOCUMENT_FIELDS, APP_NAME

class MainWindow(ctk.CTkFrame):

    def __init__(self, master=None):
        super().__init__(master, corner_radius=0) 
        
        # --- Rendre la fenetre compatible drag & drop ---
        self.tk.eval("Package require tclDND")

        # --- Configuration du Frame principal ---
        # Configuration de la grille principale du Frame (main_window)
        self.grid_rowconfigure(0, weight=0) # Pour le titre (ne s'étire pas)
        self.grid_rowconfigure(1, weight=1) # Pour le contenu (s'étire)
        self.grid_columnconfigure(0, weight=1)

        # --- Affichage du titre principal ---
        title_label = ctk.CTkLabel(self, text=f"{APP_NAME}", font=ctk.CTkFont(size=24, weight="bold"))
        title_label.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        # --- Conteneur pour les boutons de catégorie ---
        self.category_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.category_frame.grid(row=1, column=0, padx=20, pady=(0,30), sticky="n")

        # --- Zone de Glisser-Déposer (Drag & Drop) donc ligne 2, a la suite ---
        self.drop_area = ctk.CTkFrame(self, width=400, height=300, fg_color=("gray80", "gray20"))
        self.drop_area.grid(row=2, column=0, padx=50, pady=(50, 100), sticky="n") 
        self.drop_area.grid_propagate(False)
        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind('<<Drop>>', self.on_drop)

        # Texte dans la zone de glisser-déposer
        drop_label = ctk.CTkLabel(self.drop_area, text="Déposez vos fichiers PDF ici", font=ctk.CTkFont(size=18))
        drop_label.grid(row=0, column=0, padx=10, pady=100)

        self.grid_rowconfigure(0, weight=0) # Titre
        self.grid_rowconfigure(1, weight=0) # Category Frame
        self.grid_rowconfigure(2, weight=1) # Zone de drop (qui s'étire)

        # --- Génération des boutons de catégories ---
        categories = DOCUMENT_FIELDS.keys()
        col_index = 0
        for category_name in categories :
            button = ctk.CTkButton(self.category_frame, text=category_name)
            button.grid(row=0, column=col_index, padx=5, pady=5)
            col_index += 1
            
    def on_drop(self,event):
        #'event.data' contient la liste des fichiers
        print("--- FICHIERS DÉPOSÉS ---")
        print(f"Donnée brutes de l'événement : {event.data}")
        
        import re
        files_list = re.findall(r'\{[^{}]+\}|\S+', event.data)

        # Nettoyage
        cleaned_files = [f.strip('{}') for f in files_list]

        print("\nFichiers nettoyés trouvés :")
        for f in cleaned_files:
            print(f)