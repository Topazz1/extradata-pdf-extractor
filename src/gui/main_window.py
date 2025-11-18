# src/gui/main_window.py

import customtkinter as ctk
from customtkinter import filedialog # <-- NOUVEL IMPORT
from typing import List # Pour typer la liste de fichiers
from utils.config import DOCUMENT_FIELDS, APP_NAME

# On importe la future fenêtre de sélection (nous la créerons à l'étape 3.2)
from gui.extraction_window import ExtractionWindow 

class MainWindow(ctk.CTkFrame):
    
    def __init__(self, master=None):
        super().__init__(master, corner_radius=0) 

        self.grid_rowconfigure(0, weight=0) # Titre
        self.grid_rowconfigure(1, weight=0) # Boutons Catégorie
        self.grid_rowconfigure(2, weight=1) # <-- Zone principale (va s'étendre)
        self.grid_columnconfigure(0, weight=1)

        # --- Titre (Ligne 0) ---
        title_label = ctk.CTkLabel(self, text=APP_NAME, 
                                   font=ctk.CTkFont(size=24, weight="bold"))
        title_label.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        # --- Conteneur pour les boutons de catégorie (Ligne 1) ---
        self.category_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.category_frame.grid(row=1, column=0, padx=20, pady=(0, 30), sticky="n")
        
        # On stocke le type de document sélectionné (par défaut "Factures")
        self.selected_document_type = "Factures" 
        self.generate_category_buttons()

        # --- Zone Principale (Ligne 2) ---
        # On crée un Frame central pour contenir le bouton "Parcourir"
        self.main_content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_content_frame.grid(row=2, column=0, sticky="nsew")
        self.main_content_frame.grid_rowconfigure(0, weight=1)
        self.main_content_frame.grid_columnconfigure(0, weight=1)
        
        # NOUVEAU : Le bouton "Parcourir"
        self.browse_button = ctk.CTkButton(
            self.main_content_frame,
            text="Ouvrir des fichiers PDF",
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.open_file_dialog # <-- On lie le bouton à la fonction
        )
        # On le place au centre du Frame
        self.browse_button.grid(row=0, column=0, sticky="nsew", padx=100, pady=50)

    def generate_category_buttons(self):
        """ Crée les boutons de catégorie ("Factures", "CVs"...) """
        categories = DOCUMENT_FIELDS.keys()
        col_index = 0
        for category_name in categories :
            button = ctk.CTkButton(self.category_frame, text=category_name) 
            button.grid(row=0, column=col_index, padx=5, pady=5)
            col_index += 1
            # TODO: On ajoutera plus tard la logique pour changer la couleur du bouton sélectionné

    def open_file_dialog(self):
        """
        Ouvre l'explorateur de fichiers pour sélectionner des PDF.
        """
        print("Ouverture de la boîte de dialogue...")
        
        # Ouvre la fenêtre de sélection de fichiers
        # Renvoie un TUPLE de chemins de fichiers (ex: ('/path/file1.pdf', '/path/file2.pdf'))
        file_paths = filedialog.askopenfilenames(
            title="Sélectionnez des fichiers PDF",
            filetypes=[("Fichiers PDF", "*.pdf")]
        )
        
        # file_paths est un tuple, on le convertit en liste
        if file_paths:
            print(f"{len(file_paths)} fichiers sélectionnés.")
            # On lance la prochaine étape : afficher la fenêtre de sélection des champs
            self.show_extraction_window(list(file_paths))

    def show_extraction_window(self, file_paths: List[str]):
        """
        Cache la fenêtre actuelle et affiche la nouvelle fenêtre (ExtractionWindow).
        """
        # On cache le Frame principal (self)
        self.grid_forget() 
        
        # On crée une instance de la nouvelle fenêtre (que nous allons coder)
        # On lui passe la liste des fichiers et le type de document
        extraction_view = ExtractionWindow(
            master=self.master, # Le master est la fenêtre principale (l'instance 'app' de main.py)
            file_paths=file_paths,
            document_type=self.selected_document_type,
            main_menu_reference=self
        )
        # On l'affiche
        extraction_view.grid(row=0, column=0, sticky="nsew")