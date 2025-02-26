import pandas as pd
import random

# Carica il CSV dei dati degli studenti e degli esami
corso_csv = "popolamentoBD\csv\popolamento_corsi.csv"  # Percorso corretto del tuo file CSV
df_corsi = pd.read_csv(corso_csv)
corsi = df_corsi.iloc[:, 0].tolist()  # Ottieni la prima colonna

facoltà_csv = "popolamentoBD\csv\popolamento_facolta.csv"  # Percorso corretto del tuo file CSV
df_facoltà = pd.read_csv(facoltà_csv)
facoltà = df_facoltà.iloc[:, 0].tolist()  # Ottieni i nomi delle facoltà

# Funzione per generare un dataset di IstanzaDiCorso
def generate_istanza_di_corso(num):
    data = {
        "CodiceCorso": [],
        "Numero": [],
        "Anno": [],
        "Semestre": [],
        "Aula": [],
        "Giorni": [],
        "Iscritti": [],
        "Tipo": [],
        "NomeFacoltà": []
    }
    
    giorni_possibili = ["Lun", "Mar", "Mer", "Gio", "Ven"]
    
    for i in range(num):
        # Seleziona un corso casuale
        corso_selezionato = corsi[i % len(corsi)]
        
        # Genera dati casuali per l'istanza del corso
        numero = random.randint(1, 5)  # Numero casuale (1 a 5)
        anno = random.randint(2010, 2025)  # Anno casuale (2010 a 2025)
        semestre = random.randint(1, 2)  # Semestre casuale (1 o 2)
        aula = f"Aula-{random.randint(1, 30)}"  # Aula casuale (Aula-1 a Aula-10)
        # Genera un numero casuale di giorni da 1 a 4
        num_giorni = random.randint(1, 4)
        giorni_selezionati = random.sample(giorni_possibili, num_giorni)
        giorni = ", ".join(giorni_selezionati)
        iscritti = random.randint(10, 200)  # Numero casuale di iscritti (10 a 200)
        tipo = random.choice(["Normale", "A Supplenza"])  # Tipo casuale
        facoltà_selezionata = random.choice(facoltà)  # Facoltà casuale
        
        # Aggiungi i dati al dataset
        data["CodiceCorso"].append(corso_selezionato)
        data["Numero"].append(numero)
        data["Anno"].append(anno)
        data["Semestre"].append(semestre)
        data["Aula"].append(aula)
        data["Giorni"].append(giorni)
        data["Iscritti"].append(iscritti)
        data["Tipo"].append(tipo)
        data["NomeFacoltà"].append(facoltà_selezionata)

    return pd.DataFrame(data)

# Genera il dataset
istanza_di_corso_df = generate_istanza_di_corso(len(corsi))

# Scrive il DataFrame in un file CSV
output_csv = "popolamento_istanzadicorso.csv"
istanza_di_corso_df.to_csv(output_csv, index=False)

print(f"Dati popolati salvati nel file: {output_csv}")
