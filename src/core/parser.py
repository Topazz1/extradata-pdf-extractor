import re

def parse_invoice_data(text_content : str):
    found_data = {}
    
    patterns = {
        "Numero de Facture": r"Invoice No\s+.*\n\s*(\d+)",
        "Date de Facture": r"Date\s*\n.*(\d+\.\s+\w+\s+\d{4})\s*$",
        "Montant total": r"Gross Amount incl\. VAT\s*([\d.,]+)\s*€"
    }
    
    # LA CORRECTION EST ICI :
    for field_name, pattern in patterns.items(): # <--- Utilise .items()
    
        match = re.search(pattern, text_content, re.MULTILINE)
        
        if match:
            found_data[field_name] = match.group(1).strip()
        else:
            found_data[field_name] = None
    
    return found_data