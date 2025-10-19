import pdfplumber
import os

def extract_text_from_pdf(pdf_path : str):
    if not (os.path.exists(pdf_path)):
        return "Error path not exists"
    
    full_text = ""
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                full_text += page.extract_text()
                full_text += "\n"
        return full_text
        
    except Exception as e:
        print(f"Erreur lors de la lecture du PDF : {e}")
        return ""

