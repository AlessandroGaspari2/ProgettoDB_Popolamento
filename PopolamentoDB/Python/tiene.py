import pandas as pd

# Carica i CSV dei dati
docente_csv = "popolamentoBD/csv/popolamento_docenti.csv"
corso_csv = "popolamentoBD/csv/popolamento_corsi.csv"
istanza_corso_csv = "C:/Users/Rares/Downloads/popolamento_istanzadicorso_usato.csv"

try:
    df_docenti = pd.read_csv(docente_csv)
    df_corsi = pd.read_csv(corso_csv)
    df_istanza_corso = pd.read_csv(istanza_corso_csv)
except FileNotFoundError as e:
    print(f"Errore: File non trovato. {e}")
    exit(1)

# Assicurati che i dati siano consistenti
if not all(len(df) > 0 for df in [df_docenti, df_corsi, df_istanza_corso]):
    print("Errore: Uno o più file CSV sono vuoti.")
    exit(1)

# Funzione per generare un dataset di Tiene
def generate_tiene(num):
    data = {
        "NomeDocente": [],
        "CognomeDocente": [],
        "CodiceCorso": [],
        "NumeroCorso": [],
        "AnnoCorso": []
    }
    
    # Loop fino a num o la dimensione minima tra i dataset
    for i in range(num):
        try:
            nome_docente = df_docenti.iloc[i % len(df_docenti)]["Nome"]
            cognome_docente = df_docenti.iloc[i % len(df_docenti)]["Cognome"]
            codice_corso = df_istanza_corso.iloc[i % len(df_corsi)]["CodiceCorso"]
            numero_corso = int(df_istanza_corso.iloc[i % len(df_istanza_corso)]["Numero"])
            anno_corso = int(df_istanza_corso.iloc[i % len(df_istanza_corso)]["Anno"])
        except KeyError as e:
            print(f"Errore nella struttura dei CSV: {e}")
            exit(1)
        
        data["NomeDocente"].append(nome_docente)
        data["CognomeDocente"].append(cognome_docente)
        data["CodiceCorso"].append(codice_corso)
        data["NumeroCorso"].append(numero_corso)
        data["AnnoCorso"].append(anno_corso)

    return pd.DataFrame(data)

# Genera il dataset
num_righe = min(len(df_docenti), len(df_corsi), len(df_istanza_corso))
tiene_df = generate_tiene(num_righe)

# Scrive il DataFrame in un file CSV
output_csv = "popolamento_tiene.csv"
tiene_df.to_csv(output_csv, index=False)

print(f"Dati popolati salvati nel file: {output_csv}")
