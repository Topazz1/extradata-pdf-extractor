# src/main.py

import customtkinter as ctk
import sys
import os

# Ajout du répertoire parent 'src' au chemin (path)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui.main_window import MainWindow 
from utils.config import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT, COLOR_THEME, APPEARANCE_MODE

ctk.set_appearance_mode(APPEARANCE_MODE)
ctk.set_default_color_theme(COLOR_THEME)

if __name__ == "__main__":
    app = ctk.CTk() 
    
    app.title(f"{APP_NAME} - PDF Extractor")
    app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    app.resizable(False, False)
    
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    main_view = MainWindow(master=app)
    main_view.grid(row=0, column=0, sticky="nsew")

    app.mainloop()