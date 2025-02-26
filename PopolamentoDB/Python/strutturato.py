import pandas as pd
import random

# Carica il CSV dei dati degli studenti e degli esami
corso_csv = "popolamentoBD/csv/popolamento_corsi.csv"  # Percorso corretto del tuo file CSV
df_corsi = pd.read_csv(corso_csv)
corsi = df_corsi.iloc[:, 0].tolist()  # Ottieni la prima colonna

corsodilaurea_csv = "popolamentoBD/csv/popolamento_corsodilaurea.csv"  # Percorso corretto del tuo file CSV
df_corsi_di_laurea = pd.read_csv(corsodilaurea_csv)
corsidilaurea = df_corsi_di_laurea.iloc[:, 0].tolist()  # Ottieni i nomi dei corsi di laurea


# Funzione per generare un dataset di esami
def generate_strutturato(num):
    data = {
        "NomeCDL": [],
        "Codice": []
    }
    
    corsidilaurea_utilizzati = []  # Corsi di laurea già utilizzati

    for _ in range(num):
        corsidilaurea_disponibili = [m for m in corsidilaurea if m not in corsidilaurea_utilizzati]
        
        if not corsidilaurea_disponibili:
            print("Tutti i corsi di laurea sono stati utilizzati.")
            break
    
        corsidilaurea_selezionata = random.choice(corsidilaurea_disponibili)
        corsidilaurea_utilizzati.append(corsidilaurea_selezionata)  # Aggiorna l'elenco dei corsi di laurea utilizzati
        
        # Determina quanti esami il singolo studente ha sostenuto (da 12 a 24)
        num_corsidilaurea = random.randint(12, 24)
        
        corsi_usati = []
        for _ in range(num_corsidilaurea):
            # Seleziona un esame casuale finché non è unico
            corso_selezionato = random.choice(corsi)
            corsi_usati.append(corso_selezionato)
            while corso_selezionato in corsi_usati:
                corso_selezionato = random.choice(corsi)
     
            # Aggiungi i dati al dataset
            data["NomeCDL"].append(corsidilaurea_selezionata)
            data["Codice"].append(corso_selezionato)

    return pd.DataFrame(data)

# Genera il dataset
strutturato_df = generate_strutturato(len(corsidilaurea))

# Scrive il DataFrame in un file CSV
output_csv = "popolamento_strutturato.csv"
strutturato_df.to_csv(output_csv, index=False)

print(f"Dati popolati salvati nel file: {output_csv}")
