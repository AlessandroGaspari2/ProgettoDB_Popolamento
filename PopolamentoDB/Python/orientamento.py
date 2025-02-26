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

corsi_di_laurea = [f"Percorso {i}" for i in range(1, len(orientamenti_universitari) + 1)]
piano_di_studio = [f"Piano di Studio {i}" for i in range(1, len(orientamenti_universitari) + 1)]

# Funzione per generare un dataset di esami
def generate_orientamenti(num):
    data = {
        "Nome": [],
        "PianoDiStudio": [],
        "NStudenti": [],
        "NomeCDL": []
    }
    
    orientamenti_utilizzati = []  # Materie già usate

    for _ in range(num):
        orientamenti_disponibili = [m for m in orientamenti_universitari if m not in orientamenti_utilizzati]
        
        if not orientamenti_disponibili:
            print("Tutte le facolta universitarie sono state utilizzate.")
            break
    
        orientamento_selezionato = random.choice(orientamenti_disponibili)
        orientamenti_utilizzati.append(orientamento_selezionato)  # Aggiorna l'elenco delle materie utilizzate
                      
        # Seleziona un corso casuale
        corso = corsi_di_laurea.pop(0)
        piano = piano_di_studio.pop(0)
                
        # Aggiungi i dati al dataset
        data["Nome"].append(orientamento_selezionato)
        data["PianoDiStudio"].append(piano)
        data["NStudenti"].append(random.randint(100, 1000))
        data["NomeCDL"].append(corso)   
            
    return pd.DataFrame(data)

# Genera il dataset
orientamenti_df = generate_orientamenti(len(orientamenti_universitari))

# Scrive il DataFrame in un file CSV
output_csv = "popolamento_orientamenti.csv"
orientamenti_df.to_csv(output_csv, index=False)

print(f"Dati popolati salvati nel file: {output_csv}")
