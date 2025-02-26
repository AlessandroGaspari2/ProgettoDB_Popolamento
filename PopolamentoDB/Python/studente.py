import pandas as pd
from faker import Faker
import random

fake = Faker()

matricole = [random.randint(100000, 999999) for _ in range(1000)]

orientamenti_universitari = [
    "Orientamento in Data Science",
    "Orientamento in Ingegneria del Software",
    "Orientamento in Medicina",
    "Orientamento in Biotecnologie",
    "Orientamento in Marketing Digitale",
    "Orientamento in Filosofia Applicata",
    "Orientamento in Psicologia Clinica",
    "Orientamento in Scienze Ambientali",
    "Orientamento in Architettura Sostenibile",
    "Orientamento in Scienze Economiche",
    "Orientamento in Ingegneria Meccanica Avanzata",
    "Orientamento in Astrofisica",
    "Orientamento in Linguistica Computazionale",
    "Orientamento in Grafica 3D",
    "Orientamento in Filosofia Contemporanea",
    "Orientamento in Scienze della Comunicazione Interculturale",
    "Orientamento in Cyber Security",
    "Orientamento in Neuroinformatica",
    "Orientamento in Ingegneria Biomedica",
    "Orientamento in Robotica",
    "Orientamento in Economia Internazionale",
    "Orientamento in Filologia Moderna",
    "Orientamento in Scienze della Formazione Digitale",
    "Orientamento in Diritto Internazionale",
    "Orientamento in Pedagogia Sperimentale",
    "Orientamento in Scienze Politiche Comparate",
    "Orientamento in Biochimica",
    "Orientamento in Design Industriale",
    "Orientamento in Ingegneria Civile",
    "Orientamento in Biologia Marina",
    "Orientamento in Marketing e Social Media",
    "Orientamento in Scienze Sociali per la Globalizzazione",
    "Orientamento in Grafica Pubblicitaria",
    "Orientamento in Logistica e Supply Chain Management",
    "Orientamento in Biostatistica",
    "Orientamento in Scienze Geologiche Applicate",
    "Orientamento in Economia Aziendale",
    "Orientamento in Filosofia del Linguaggio",
    "Orientamento in Ingegneria Elettrica",
    "Orientamento in Economia e Finanza",
    "Orientamento in Design del Prodotto",
    "Orientamento in Scienze della Nutrizione",
    "Orientamento in Data Visualization",
    "Orientamento in Scienze dei Materiali",
    "Orientamento in Intelligenza Artificiale per la Salute",
    "Orientamento in Didattica per l’Inclusione",
    "Orientamento in Ingegneria dei Trasporti",
    "Orientamento in Scienze della Cultura Digitale",
    "Orientamento in Neuropsicologia",
    "Orientamento in Scienze della Comunicazione Politica",
    "Orientamento in Economia e Commercio Internazionale",
    "Orientamento in Psicologia Cognitiva Applicata"
]

# Funzione per generare un dataset di esami
def generate_studenti(num):
    data = {
        "Matricola": [],
        "Nome": [],
        "Indirizzo": [],
        "AnnoImmatricolazione": [],
        "Status": [],
        "NomeOrientamento": []
    }
    
    matricole_utilizzati = []

    for _ in range(num):
        matricole_disponibili = [m for m in matricole if m not in matricole_utilizzati]
        
        if not matricole_disponibili:
            print("Tutte le facolta universitarie sono state utilizzate.")
            break
    
        matricole_selezionate = random.choice(matricole_disponibili)
        matricole_utilizzati.append(matricole_selezionate)  # Aggiorna l'elenco delle materie utilizzate
                      
        # Seleziona un corso casuale
        matricola = matricole.pop(0)
                
        # Aggiungi i dati al dataset
        data["Matricola"].append(matricola)
        data["Nome"].append(fake.first_name())
        data["Indirizzo"].append(fake.address().replace('\n', ', '))
        data["AnnoImmatricolazione"].append(random.randint(2010, 2024))
        data["Status"].append(random.choice(['Attivo', 'Inattivo', 'Sospeso']))
        data["NomeOrientamento"].append(random.choice(orientamenti_universitari))
      
            
    return pd.DataFrame(data)

# Genera il dataset
studenti_df = generate_studenti(len(matricole))

# Scrive il DataFrame in un file CSV
output_csv = "popolamento_studenti.csv"
studenti_df.to_csv(output_csv, index=False)

print(f"Dati popolati salvati nel file: {output_csv}")
