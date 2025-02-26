import pandas as pd
import random

# Leggi il file CSV delle facoltà
facolta_csv = "popolamento_facolta_gruppi.csv"  # Percorso corretto del tuo file CSV
df_facolta = pd.read_csv(facolta_csv)

facolta = df_facolta.iloc[:, 0].tolist()  # Ottieni la prima colonna con i nomi delle facoltà
gruppo = df_facolta.iloc[:, 1].tolist()  # Ottieni la prima colonna con i nomi delle facoltà

# Funzione per generare un dataset di facoltà
def generate_istanza_di_corso(num):
    data = {
        "Nome": [],  # Nome della facoltà
        "Numero": [],  # Numero casuale tra 1 e 20
        "IDSedi": []  # Gruppo delle sedi
    }
    
    facolta_utilizzate = []  # Lista per non usare due volte la stessa facoltà
    
    for i in range(num):
        facolta_disponibili = [m for m in facolta if m not in facolta_utilizzate]
        
        if not facolta_disponibili:
            print("Tutte le facoltà universitarie sono state utilizzate.")
            break
        
        # Seleziona un nome di facoltà dal CSV
        facolta_selezionata = facolta[i]
        facolta_utilizzate.append(facolta_selezionata)
        gruppo_selezionato = gruppo[i]
        
        sedi_utilizzate = []
        sedi_facolta = random.randint(1, 5)  
        
        for _ in range(sedi_facolta):
            sedi = random.randint(1, 20)    
            while sedi in sedi_utilizzate:
                sedi = random.randint(1, 20)   
                             
            data["Nome"].append(facolta_selezionata)
            data["Numero"].append(sedi)
            data["IDSedi"].append(gruppo_selezionato)
    
    return pd.DataFrame(data)

# Genera il dataset con facoltà e relative informazioni
facolta_df = generate_istanza_di_corso(len(facolta))

# Scrive il DataFrame in un file CSV
output_csv = "popolamento_sede_con_gruppi.csv"
facolta_df.to_csv(output_csv, index=False)

print(f"Dati popolati salvati nel file: {output_csv}")
