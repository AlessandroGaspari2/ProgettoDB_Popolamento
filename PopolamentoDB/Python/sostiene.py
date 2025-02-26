import pandas as pd
import random

# Carica il CSV dei dati degli studenti e degli esami
studenti_csv = "popolamentoBD\csv\popolamento_studenti.csv"  # Sostituisci con il percorso corretto del tuo file CSV
df_studenti = pd.read_csv(studenti_csv)
matricole = df_studenti.iloc[:, 0].tolist()  # Ottieni la prima colonna

esami_csv = "popolamentoBD\csv\popolamento_esami.csv"  # Sostituisci con il percorso corretto del tuo file CSV
df_esami = pd.read_csv(esami_csv)
esami = df_esami.iloc[:, 0].tolist()  # Ottieni i nomi degli esami


# Funzione per generare un dataset di esami
def generate_sostiene(num):
    data = {
        "Matricola": [],
        "Esame": []
    }
    
    matricole_utilizzati = []  # Matricole già utilizzate

    for _ in range(num):
        matricole_disponibili = [m for m in matricole if m not in matricole_utilizzati]
        
        if not matricole_disponibili:
            print("Tutte le matricole sono state utilizzate.")
            break
    
        matricola_selezionata = random.choice(matricole_disponibili)
        matricole_utilizzati.append(matricola_selezionata)  # Aggiorna l'elenco delle matricole utilizzate
        
        esami_sostenuti = set()  # Esami già sostenuti dallo studente
        
        # Determina quanti esami il singolo studente ha sostenuto (da 0 a 18)
        num_esami = random.randint(0, 18)
        
        for _ in range(num_esami):
            # Seleziona un esame casuale finché non è unico
            esame_selezionato = random.choice(esami)
            while esame_selezionato in esami_sostenuti:
                esame_selezionato = random.choice(esami)
            esami_sostenuti.add(esame_selezionato)
            
            # Aggiungi i dati al dataset
            data["Matricola"].append(matricola_selezionata)
            data["Esame"].append(esame_selezionato)

    return pd.DataFrame(data)

# Genera il dataset
sostiene_df = generate_sostiene(len(matricole))

# Scrive il DataFrame in un file CSV
output_csv = "popolamento_sostiene.csv"
sostiene_df.to_csv(output_csv, index=False)

print(f"Dati popolati salvati nel file: {output_csv}")
