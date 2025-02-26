import pandas as pd
import random

materie_universitarie = [
    "Informatica", "Fisica", "Chimica", "Matematica", "Ingegneria Informatica",
    "Economia", "Scienze della Comunicazione", "Psicologia", "Biologia", "Sociologia",
    "Lettere e Filosofia", "Scienze Politiche", "Scienze Ambientali", "Geologia", 
    "Architettura", "Medicina", "Farmacia", "Odontoiatria", "Scienze Biologiche", 
    "Scienze Geografiche", "Statistica", "Scienze dei Materiali", "Scienze della Formazione", 
    "Scienze Naturali", "Ingegneria Meccanica", "Ingegneria Elettronica", "Ingegneria Civile", 
    "Ingegneria Biomedica", "Lingue Straniere", "Storia dell’Arte", "Marketing", 
    "Sociologia del Lavoro", "Diritto Privato", "Diritto Pubblico", "Economia Aziendale",
    "Statistica Sociale", "Scienza Politica", "Geografia Economica", "Filosofia della Scienza", 
    "Bioinformatica", "Neuroscienze", "Fisiologia", "Epidemiologia", "Astrofisica", "Informatica Teorica",
    "Calcolo Numerico", "Programmazione Logica", "Machine Learning", "Intelligenza Artificiale", 
    "Economia dell'Ambiente", "Diritto Internazionale", "Psicologia del Lavoro", "Psicopatologia", 
    "Farmacologia", "Immunologia", "Biochimica", "Genetica", "Scienze Veterinarie", "Scienze alimentari"
]

# Funzione per generare un dataset di esami
def generate_exams(materie):
    data = {
        "Nome": [],
        "NCrediti": []
    }
    
    materie_utilizzate = set()  # Materie già usate

    while len(materie_utilizzate) < len(materie):
        # Seleziona una materia non ancora utilizzata
        materia_selezionata = random.choice(materie)
        if materia_selezionata not in materie_utilizzate:
            materie_utilizzate.add(materia_selezionata)
            
            # Aggiungi la materia con un numero di crediti casuale
            data["Nome"].append(materia_selezionata)
            data["NCrediti"].append(random.randint(2, 18))  # Crediti tra 6 e 12
            
    return pd.DataFrame(data)

# Genera il dataset
exams_df = generate_exams(materie_universitarie)

# Scrive il DataFrame in un file CSV
output_csv = "popolamento_esami.csv"
exams_df.to_csv(output_csv, index=False)

print(f"Dati popolati salvati nel file: {output_csv}")
