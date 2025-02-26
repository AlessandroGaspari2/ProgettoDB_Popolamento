import pandas as pd
import random

facolta_universitarie = [
    "Facoltà di Informatica", "Facoltà di Matematica", "Facoltà di Fisica", 
    "Facoltà di Chimica", "Facoltà di Biologia", "Facoltà di Medicina", 
    "Facoltà di Farmacia", "Facoltà di Economia", "Facoltà di Giurisprudenza", 
    "Facoltà di Ingegneria Informatica", "Facoltà di Ingegneria Meccanica", 
    "Facoltà di Ingegneria Elettronica", "Facoltà di Ingegneria Civile", 
    "Facoltà di Ingegneria Biomedica", "Facoltà di Psicologia", 
    "Facoltà di Scienze della Comunicazione", "Facoltà di Scienze Politiche", 
    "Facoltà di Scienze Naturali", "Facoltà di Scienze Ambientali", 
    "Facoltà di Geologia", "Facoltà di Scienze dei Materiali", 
    "Facoltà di Scienze Statistiche", "Facoltà di Architettura", 
    "Facoltà di Filosofia", "Facoltà di Storia", "Facoltà di Lettere e Filosofia", 
    "Facoltà di Sociologia", "Facoltà di Antropologia", "Facoltà di Diritto Internazionale", 
    "Facoltà di Lingue e Letterature Straniere", "Facoltà di Scienze Motorie", 
    "Facoltà di Scienze Veterinarie", "Facoltà di Scienze Agrarie", 
    "Facoltà di Scienze e Tecnologie Alimentari", "Facoltà di Pedagogia", 
    "Facoltà di Scienze della Formazione", "Facoltà di Astrofisica", 
    "Facoltà di Economia Aziendale", "Facoltà di Statistica Economica", 
    "Facoltà di Marketing e Comunicazione", "Facoltà di Diritto Pubblico", 
    "Facoltà di Diritto Privato", "Facoltà di Logistica e Trasporti", 
    "Facoltà di Design Industriale", "Facoltà di Urbanistica", 
    "Facoltà di Scienze Geografiche", "Facoltà di Neuroscienze", 
    "Facoltà di Bioinformatica", "Facoltà di Biochimica", "Facoltà di Genetica", 
    "Facoltà di Immunologia", "Facoltà di Farmacologia", 
    "Facoltà di Psicopatologia", "Facoltà di Psicologia del Lavoro", 
    "Facoltà di Intelligenza Artificiale", "Facoltà di Machine Learning", 
    "Facoltà di Informatica Teorica", "Facoltà di Calcolo Numerico", 
    "Facoltà di Programmazione Logica"
]



sedi = [f"Edificio {i}" for i in range(1, 21)]

def generate_facolta(num):
    data = {
        "Nome": [],
        "Sede": [],
        "Telefono": []
    }
    
    facolta_utilizzate = []

    for i in range(num):
        facolta_disponibili = [m for m in facolta_universitarie if m not in facolta_utilizzate]
        
        facolta = facolta_universitarie[i]
                  
        # Seleziona un telefono e una sede 
        sede = f"Gruppo-{i}"
        telefono = f"Telefoni-{i}"
        
        data["Nome"].append(facolta)
        data["Sede"].append(sede)
        data["Telefono"].append(telefono)
    
    return pd.DataFrame(data)

# Genera il dataset
facolta_df = generate_facolta(len(facolta_universitarie))

# Scrive il DataFrame in un file CSV
output_csv = "popolamento_facolta_gruppi.csv"
facolta_df.to_csv(output_csv, index=False)

print(f"Dati popolati salvati nel file: {output_csv}")
