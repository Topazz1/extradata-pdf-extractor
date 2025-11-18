# src/core/extractor.py

import pdfplumber
import os
import pytesseract
from pdf2image import convert_from_path
import tempfile # Pour gérer les images temporaires de l'OCR


class Extractor:
    """
    Extrait le texte brut d'un fichier PDF.
    Tente d'abord une extraction rapide (pdfplumber),
    puis utilise l'OCR (pytesseract) si la première échoue.
    """
    
    def __init__(self):
        # Sur Windows, peut-être spécifier le chemin de Tesseract
        # ex: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pass

    def _extract_text_with_ocr(self, pdf_path: str) -> str:
        """
        Méthode de SECOURS (privée) : Extrait le texte via Tesseract OCR.
        C'est le code que nous avons validé dans notre fichier test.
        """
        full_ocr_text = ""
        
        try:
            with tempfile.TemporaryDirectory() as path:
                # Convertit le PDF en une liste d'images (PIL)
                images = convert_from_path(pdf_path, 
                                           output_folder=path, 
                                           fmt='png', 
                                           dpi=300) # 300dpi pour une meilleure reconnaissance
                
                # Parcourt chaque image/page et applique l'OCR
                for image in images:
                    # C'est la fonction clé : Tesseract lit l'image
                    text_from_ocr = pytesseract.image_to_string(image, lang='fra') # On spécifie 'fra' pour le français
                    full_ocr_text += text_from_ocr + "\n"
            
            return full_ocr_text

        except Exception as e:
            print(f"Erreur OCR : {e}")
            return "" # Renvoie une chaîne vide en cas d'échec de l'OCR


    def extract_text(self, file_path: str) -> str:
        """
        Méthode PRINCIPALE (publique) : Tente d'extraire le texte.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Fichier non trouvé : {file_path}")

        full_text = ""
        
        # --- Essai 1: Pdfplumber (Rapide) ---
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text: # S'assurer que du texte a été trouvé
                        full_text += page_text + "\n"
        
        except Exception as e:
            print(f"Erreur Pdfplumber : {e}")
            full_text = "" # Réinitialise en cas d'erreur (ex: PDF corrompu)

        # --- Vérification et Essai 2: OCR (Secours) ---
        
        # Si le texte est très court, on suppose que c'est un scan
        if len(full_text.strip()) < 50: 
            print("Pdfplumber n'a trouvé que peu de texte. Tentative OCR...")
            full_text = self._extract_text_with_ocr(file_path)
        
        return full_text