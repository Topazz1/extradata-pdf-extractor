# src/gui/extraction_window.py

import customtkinter as ctk
import threading
import os
from typing import List, Dict, Any
from utils.config import DOCUMENT_FIELDS 
from core.extractor import Extractor
from core.parser import Parser
from core.csv_generator import CSVGenerator
from utils.file_manager import FileManager

class ExtractionWindow(ctk.CTkFrame):
    
    # Ajoutez main_menu_reference aux arguments
    def __init__(self, master, file_paths: List[str], document_type: str, main_menu_reference):
        super().__init__(master, corner_radius=0)
        
        self.file_paths = file_paths
        self.document_type = document_type
        self.main_menu = main_menu_reference # Pour pouvoir revenir en arrière
        
        self.possible_fields = DOCUMENT_FIELDS.get(document_type, [])
        self.field_switches: Dict[str, ctk.CTkSwitch] = {} 
        
        self.extractor = Extractor()
        self.parser = Parser(document_type=self.document_type)
        self.csv_generator = CSVGenerator()
        self.file_manager = FileManager()

        # Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1) # On ajoute une colonne pour la liste des fichiers
        self.grid_rowconfigure(1, weight=1) 

        # --- Titre et Bouton Retour (Ligne 0) ---
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=20)
        
        # Bouton Retour
        back_btn = ctk.CTkButton(header_frame, text="< Retour", width=80, command=self.go_back_to_menu)
        back_btn.pack(side="left")
        
        title_label = ctk.CTkLabel(header_frame, text="Configuration & Extraction", 
                                   font=ctk.CTkFont(size=24, weight="bold"))
        title_label.pack(side="left", padx=20)

        # --- COLONNE GAUCHE : Sélection des champs ---
        left_frame = ctk.CTkFrame(self)
        left_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        ctk.CTkLabel(left_frame, text="Champs à extraire", font=ctk.CTkFont(weight="bold")).pack(pady=10)
        
        self.fields_container = ctk.CTkFrame(left_frame, fg_color="transparent")
        self.fields_container.pack(fill="both", expand=True)
        self.create_field_switches()

        # --- COLONNE DROITE : Liste des fichiers (NOUVEAU !) ---
        right_frame = ctk.CTkFrame(self)
        right_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        
        ctk.CTkLabel(right_frame, text=f"Fichiers sélectionnés ({len(self.file_paths)})", 
                     font=ctk.CTkFont(weight="bold")).pack(pady=10)
        
        # Zone scrollable pour les fichiers
        self.file_list_scroll = ctk.CTkScrollableFrame(right_frame, label_text="Liste")
        self.file_list_scroll.pack(fill="both", expand=True, padx=10, pady=10)
        
        for f in self.file_paths:
            lbl = ctk.CTkLabel(self.file_list_scroll, text=os.path.basename(f), anchor="w")
            lbl.pack(fill="x", padx=5)

        # --- BAS : Bouton Lancer et Logs ---
        bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        bottom_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=20)
        
        self.launch_button = ctk.CTkButton(
            bottom_frame,
            text="Lancer l'extraction",
            font=ctk.CTkFont(size=18, weight="bold"),
            height=50,
            command=self.launch_extraction_thread
        )
        self.launch_button.pack(fill="x")
        
        self.results_textbox = ctk.CTkTextbox(self, state="disabled", height=100)
        self.results_textbox.grid(row=3, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="ew")

    def create_field_switches(self):
        for field_name in self.possible_fields:
            frame = ctk.CTkFrame(self.fields_container, fg_color="transparent")
            frame.pack(fill="x", pady=5, padx=10)
            
            lbl = ctk.CTkLabel(frame, text=field_name)
            lbl.pack(side="left")
            
            switch = ctk.CTkSwitch(frame, text="")
            switch.select()
            switch.pack(side="right")
            
            self.field_switches[field_name] = switch

    def go_back_to_menu(self):
        """ Cache cette fenêtre et réaffiche le menu principal """
        self.grid_forget() # On se cache
        self.main_menu.grid(row=0, column=0, sticky="nsew") # On réaffiche le menu

    def launch_extraction_thread(self):
        self.launch_button.configure(state="disabled", text="Extraction en cours...")
        self.thread = threading.Thread(target=self.start_extraction_process, daemon=True)
        self.thread.start()

    def start_extraction_process(self):
        all_results = []
        try:
            self.log_message("--- Analyse en cours ---")
            selected_fields = [fn for fn, sw in self.field_switches.items() if sw.get() == 1]
            self.parser.fields_to_find = selected_fields
            
            for i, file_path in enumerate(self.file_paths):
                self.log_message(f"({i+1}/{len(self.file_paths)}) Traitement : {os.path.basename(file_path)}")
                
                raw_text = self.extractor.extract_text(file_path)
                parsed_data = self.parser.parse_text_data(raw_text)
                parsed_data["Source Fichier"] = os.path.basename(file_path)
                
                all_results.append(parsed_data)
            
            self.log_message("--- Terminé ! Enregistrement... ---")
            self.show_save_dialog_and_export(all_results)
            
        except Exception as e:
            self.log_message(f"ERREUR : {e}")
        finally:
            self.launch_button.configure(state="normal", text="Lancer l'extraction")

    def show_save_dialog_and_export(self, all_results):
        save_path = self.file_manager.get_save_path_for_csv()
        if save_path:
            if self.csv_generator.generate_csv(all_results, save_path):
                self.log_message(f"SUCCÈS ! Fichier enregistré : {os.path.basename(save_path)}")
                # Optionnel : Proposer de revenir au menu automatiquement
                # self.after(2000, self.go_back_to_menu) 
        else:
            self.log_message("Enregistrement annulé.")

    def log_message(self, message: str):
        self.results_textbox.configure(state="normal")
        self.results_textbox.insert("end", message + "\n")
        self.results_textbox.configure(state="disabled")
        self.results_textbox.see("end")