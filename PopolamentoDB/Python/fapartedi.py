import pandas as pd
import random

# Carica il CSV dei dati degli studenti e degli esami
orientamenti_csv = "popolamentoBD\csv\popolamento_orientamenti.csv"  # Percorso corretto del tuo file CSV
df_orientamenti = pd.read_csv(orientamenti_csv)
orientamenti = df_orientamenti.iloc[:, 0].tolist()  # Ottieni i nomi degli orientamenti

esami_csv = "popolamentoBD\csv\popolamento_esami.csv"  # Percorso corretto del tuo file CSV
df_esami = pd.read_csv(esami_csv)
esami = df_esami.iloc[:, 0].tolist()  # Ottieni i nomi degli esami


# Funzione per generare un dataset di esami
def generate_fapartedi(num):
    data = {
        "NomeEsame": [],
        "NomeOrientamento": []
    }
    
    esami_utilizzati = set()  # Matricole già utilizzate

    for _ in range(num):
        esami_disponibili = [m for m in esami if m not in esami_utilizzati]
        
        if not esami_disponibili:
            print("Tutti gli esami sono stati utilizzati.")
            break
    
        esame_selezionato = random.choice(esami_disponibili)
        orientamenti_selezionati = random.choice(orientamenti)
        esami_utilizzati.add(esame_selezionato)  # Aggiorna l'elenco degli esami utilizzati
        
        # Seleziona un orientamento casuale
        data["NomeEsame"].append(esame_selezionato)
        data["NomeOrientamento"].append(orientamenti_selezionati)

    return pd.DataFrame(data)

try:
    # Genera il dataset
    fapartedi_df = generate_fapartedi(len(esami))
    
    # Scrive il DataFrame in un file CSV
    output_csv = "popolamento_fapartedi.csv"
    fapartedi_df.to_csv(output_csv, index=False)
    print(f"Dati popolati salvati nel file: {output_csv}")
except Exception as e:
    print(f"Errore durante la scrittura del CSV: {e}")
