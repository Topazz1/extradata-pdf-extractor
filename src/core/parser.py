# src/core/parser.py

import re
from typing import Dict, Any
from utils.config import DOCUMENT_FIELDS

class Parser:
    def __init__(self, document_type: str = "Factures"):
        self.fields_to_find = DOCUMENT_FIELDS.get(document_type, [])
        self.patterns = self._get_patterns_for_type(document_type)

    def _get_patterns_for_type(self, document_type: str) -> Dict[str, str]:
        if document_type == "Factures":
            return {
                "Numéro de Facture": r"(?:Facture N°|N° de facture|Réf\.|N° de compte)\s*[:\s]*([A-Z0-9-]+)",
                "Nom du Client": r"(?:Client|Nom|N° client)\s*[:\s]*([A-Z0-9\s]+)",
                "Date de Facture": r"(\d{2}[/.-]\d{2}[/.-]\d{2,4})",
                "Montant Total": r"(?:Total TTC|TOTAL|Montant Total|Montant total TTC)[\s\S]*?([\d\s.,]+)€?",
                "Adresse": r"(\d{5}\s[A-Z\s]+)"
            }
        return {}

    def parse_text_data(self, raw_text: str) -> Dict[str, Any]:
        results: Dict[str, Any] = {}
        # On garde les sauts de ligne car ils sont importants pour la structure
        # On enlève juste les caractères bizarres
        
        for field, pattern in self.patterns.items():
            if field not in self.fields_to_find:
                continue

            # Recherche flexible
            match = re.search(pattern, raw_text, re.IGNORECASE | re.MULTILINE)
            
            if match:
                # Nettoyage du résultat (enlève les sauts de ligne dans la valeur capturée)
                clean_value = match.group(1).replace('\n', ' ').strip()
                results[field] = clean_value
            else:
                results[field] = "Non trouvé"

        return results