import pandas as pd
from faker import Faker
import random

fake = Faker()

materie_universitarie = [
    "Informatica", "Fisica", "Chimica", "Matematica", "Ingegneria Informatica",
    "Economia", "Scienze della Comunicazione", "Psicologia", "Biologia", "Sociologia",
    "Lettere e Filosofia", "Scienze Politiche", "Scienze Ambientali", "Geologia", 
    "Architettura", "Medicina", "Farmacia", "Odontoiatria", "Scienze Biologiche", 
    "Scienze Geografiche", "Statistica", "Scienze dei Materiali", "Scienze della Formazione", 
    "Scienze Naturali", "Ingegneria Meccanica", "Ingegneria Elettronica", "Ingegneria Civile", 
    "Ingegneria Biomedica", "Lingue Straniere", "Storia dell’Arte", "Marketing", "Sociologia del Lavoro", "Diritto Privato", "Diritto Pubblico", "Economia Aziendale",
    "Statistica Sociale", "Scienza Politica", "Geografia Economica", "Filosofia della Scienza", 
    "Bioinformatica", "Neuroscienze", "Fisiologia", "Epidemiologia", "Astrofisica", "Informatica Teorica",
    "Calcolo Numerico", "Programmazione Logica", "Machine Learning", "Intelligenza Artificiale", 
    "Economia dell'Ambiente", "Diritto Internazionale", "Psicologia del Lavoro", "Psicopatologia", 
    "Farmacologia", "Immunologia", "Biochimica", "Genetica", "Scienze Veterinarie", "Scienze alimentari"
]

# Funzione per generare un dataset di corsi
def generate_courses(num):
    data = {
        "Codice": [],
        "Nome": [],
        "Durata": [],
        "Descrizione": [],
        "NModuli": []
    }
    
    materie_utilizzate = []  # Materie che sono già state utilizzate
    
    for _ in range(num):  # Genera 'num' record
        # Lista di materie ancora non utilizzate
        materie_disponibili = [m for m in materie_universitarie if m not in materie_utilizzate]
        
        if not materie_disponibili:
            print("Tutte le materie universitarie sono state utilizzate.")
            break
    
    materia_selezionata = random.choice(materie_disponibili)
    materie_utilizzate.append(materia_selezionata)  # Aggiorna l'elenco delle materie utilizzate
        
    for _ in range(num):  # Genera 'num' record
        data["Codice"].append(random.randint(1000, 9999))
        data["Nome"].append(random.choice(materie_universitarie))
        data["Durata"].append(random.randint(1, 12))  
        data["Descrizione"].append(fake.text(max_nb_chars=100))
        data["NModuli"].append(random.randint(1, 2))
        
    return pd.DataFrame(data)

# Genera un dataset di 1000 corsi
courses_df = generate_courses(len(materie_universitarie))

# Scrive il DataFrame in un file CSV
output_csv = "popolamento_corsi.csv"
courses_df.to_csv(output_csv, index=False)

print(f"Dati popolati salvati nel file: {output_csv}")
