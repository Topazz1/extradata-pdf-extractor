# 📄 Extradata // Automated PDF Extraction Pipeline

> A modular desktop utility built with **Python**, **CustomTkinter**, **pdfplumber**, and **Pandas** to ingest unstructured PDF documents (invoices, resumes, administrative files) and automatically extract key business entities into structured tabular data.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](#)
[![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blue?style=flat-square)](#)
[![pdfplumber](https://img.shields.io/badge/Parser-pdfplumber-yellow?style=flat-square)](#)
[![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=flat-square&logo=pandas&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#)

---

## 📌 Overview

Manual extraction of financial indicators and contract metadata from PDF invoices is repetitive, error-prone, and time-intensive. **Extradata** provides a lightweight, configuration-driven desktop interface that standardizes data extraction pipelines across multiple document categories.

```text
 ┌─────────────────┐
 │   PDF Ingestion │ (Drag & Drop / File Input)
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │ Parsing Pipeline│ ◄── [Schema Config: DOCUMENT_FIELDS]
 │  (pdfplumber)   │     - Total Amount, Invoice Date, ID, Client
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │ Structured Data │ ───► [CustomTkinter GUI / DataFrame Output]
 │    (Pandas)     │
 └─────────────────┘

```

---

## ⚡ Key Features

* **Schema-Driven Extraction:** Extraction schemas are defined declaratively in `config.py` (`DOCUMENT_FIELDS`), allowing rapid adaptation to new document classes (e.g., invoices, CVs, contracts) without altering core parsing logic.

* **Dynamic Category Selection:** The GUI automatically discovers configured document types and dynamically renders filtering and processing actions.

* **Modern Desktop Interface:** Built on `CustomTkinter` with adaptive system appearance detection (Dark/Light mode) and a high-contrast drag-and-drop staging zone.

* **Tabular Data Processing:** Integrates `pandas` to clean, normalize, and prepare extracted document records for direct downstream analytics or CSV/Excel exports.



---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.10+
* **GUI Framework:** [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) for responsive, theme-aware desktop windows

* **Document Ingestion:** [`pdfplumber`](https://github.com/jsvine/pdfplumber) for robust text layout rendering and character extraction

* **Data Engineering:** [`pandas`](https://pandas.pydata.org/) for schema enforcement and data structuring



---

## 📂 Architecture & Directory Structure

```text
extradata-pdf-extractor/
├── src/
│   ├── gui/
│   │   └── main_window.py     # Main layout, drop zone & category controls
│   ├── utils/
│   │   └── config.py          # App settings, window geometry & extraction schemas
│   └── main.py                # Application entrypoint & runtime initialization
├── requirements.txt           # Production dependencies
└── README.md

```

---

## 🚀 Quick Start

### 1. Prerequisites

Ensure you have Python 3.10 or newer installed:

```bash
python --version

```

### 2. Clone Repository & Setup Environment

```bash
git clone [https://github.com/Topazz1/extradata-pdf-extractor.git](https://github.com/Topazz1/extradata-pdf-extractor.git)
cd extradata-pdf-extractor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run Application

```bash
python src/main.py

```

---

## ⚙️ Configuration & Schema Customization

Document schemas and extraction targets are maintained inside `src/utils/config.py`:

```python
DOCUMENT_FIELDS = {
    "Factures": [
        "Montant total",
        "Date de Facture",
        "Numero de Facture",
        "Nom du client",
        "Adresse"
    ],
    "CVs": [
        "Nom",
        "Email",
        "Compétences"
    ],
    "Autres documents": []
}

```

New categories added to `DOCUMENT_FIELDS` will automatically instantiate corresponding selector buttons in the application control bar.

---

## 👤 Author

**Tom Padovani**

Computer Science & Socio-Technical Systems (Hutech) Engineering Student — **UTC Compiègne**

* LinkedIn: [@tom-padovani](https://www.linkedin.com/in/tom-padovani-2b0b87382/)
* GitHub: [@tomPadovani](https://github.com/Topazz1)
