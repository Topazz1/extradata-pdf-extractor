import customtkinter as ctk

# MainWindow doit maintenant hériter de ctk.CTkFrame
class MainWindow(ctk.CTkFrame): # <-- Changement : CTkFrame au lieu de CTk
    
    # master représente la fenêtre principale (l'instance 'app' de main.py)
    def __init__(self, master=None):
        # Appelle le constructeur de CTkFrame (le conteneur)
        # On s'assure qu'il prenne toute la place dans la fenêtre parente (master)
        super().__init__(master, corner_radius=0) 

        # --- Configuration du Frame principal ---
        # Notez que nous enlevons ici les lignes de configuration de fenêtre 
        # (self.title, self.geometry, self.resizable) car elles sont maintenant 
        # dans main.py et s'appliquent à 'app'.

        # Configuration de la grille principale du Frame (main_window)
        self.grid_rowconfigure(0, weight=0) # Pour le titre (ne s'étire pas)
        self.grid_rowconfigure(1, weight=1) # Pour le contenu (s'étire)
        self.grid_columnconfigure(0, weight=1)

        # --- Affichage du titre principal ---
        # (Reste inchangé, mais on le place dans le Frame)
        title_label = ctk.CTkLabel(self, text="Extradata", 
                                   font=ctk.CTkFont(size=24, weight="bold"))
        # Place le label en haut du Frame (ligne 0)
        title_label.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        # --- Zone de Glisser-Déposer (Drag & Drop) ---
        self.drop_area = ctk.CTkFrame(self, width=400, height=300, 
                                      fg_color=("gray80", "gray20"))
        
        # Le drop_area est maintenant placé en ligne 1 (la ligne étirable)
        # 'n' : nord, le fait coller au haut de la ligne 1
        self.drop_area.grid(row=1, column=0, padx=50, pady=(50, 100), sticky="n") 
        self.drop_area.grid_propagate(False)

        # Texte dans la zone de glisser-déposer
        drop_label = ctk.CTkLabel(self.drop_area, 
                                  text="Déposez vos fichiers PDF ici", 
                                  font=ctk.CTkFont(size=18))
        drop_label.grid(row=0, column=0, padx=10, pady=100)