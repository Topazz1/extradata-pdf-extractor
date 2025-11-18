# src/core/csv_generator.py

import pandas as pd
from typing import List, Dict, Any

class CSVGenerator:
    """
    Classe responsable de la conversion des données extraites en format CSV.
    """
    def __init__(self):
        pass

    def generate_csv(self, all_results: List[Dict[str, Any]], output_path: str):
        """
        Convertit une liste de dictionnaires de résultats en un fichier CSV.
        
        :param all_results: Liste des dictionnaires de données analysées.
        :param output_path: Chemin complet où enregistrer le fichier CSV.
        """
        if not all_results:
            raise ValueError("Aucune donnée à exporter n'a été fournie.")

        try:
            # 1. Crée un DataFrame Pandas à partir de la liste de dictionnaires
            df = pd.DataFrame(all_results)
            
            # 2. Sauvegarde le DataFrame en CSV
            # index=False pour ne pas inclure la colonne d'index de Pandas
            df.to_csv(output_path, index=False, encoding='utf-8')
            
            return True

        except Exception as e:
            raise Exception(f"Erreur lors de la génération du CSV : {e}")