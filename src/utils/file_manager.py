# src/utils/file_manager.py

from customtkinter import filedialog

class FileManager:
    """
    Gère les boîtes de dialogue de fichiers et chemins d'accès.
    """
    def __init__(self):
        pass

    def get_save_path_for_csv(self) -> str | None:
        """
        Ouvre une boîte de dialogue pour demander à l'utilisateur où enregistrer le CSV.
        
        :return: Le chemin complet du fichier de sauvegarde, ou None si annulé.
        """
        # filedialog.asksaveasfilename est parfait pour demander où enregistrer
        save_path = filedialog.asksaveasfilename(
            defaultextension=".csv", # Ajoute .csv si l'utilisateur ne le fait pas
            initialfile="resultats_extraction.csv",
            title="Enregistrer le fichier de résultats CSV",
            filetypes=[("Fichiers CSV", "*.csv")]
        )
        return save_path