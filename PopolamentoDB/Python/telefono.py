import pandas as pd
import random

# Leggi il file CSV delle facoltà
facolta_csv = "popolamento_facolta_gruppi.csv"  # Percorso corretto del tuo file CSV
df_facolta = pd.read_csv(facolta_csv)

facolta = df_facolta.iloc[:, 0].tolist()  # Ottieni la prima colonna con i nomi delle facoltà
gruppo = df_facolta.iloc[:, 2].tolist()  # Ottieni la prima colonna con i nomi delle facoltà

numeri_telefonici = [
    "+393201234567", "+393409876543", "+393507654321", "+393602345678",
    "+393708765432", "+393803456789", "+393906543210", "+393104567890",
    "+393305678901", "+393006789012"
]

# Funzione per generare un dataset di facoltà
def generate_istanza_di_corso(num):
    data = {
        "Nome": [],  # Nome della facoltà
        "Numero": [],  # Numero casuale tra 1 e 20
        "IDGruppi": []  # Gruppo delle sedi
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
        
        telefoni_utilizzati = []
        telefoni_facolta = random.randint(1, 5)  
        
        for _ in range(telefoni_facolta):
            telefono = random.choice(numeri_telefonici)  # Seleziona un numero telefonico a caso
            while telefono in telefoni_utilizzati:  # Se il numero è già stato utilizzato, seleziona un altro numero
                telefono = random.choice(numeri_telefonici)
            
            data["Nome"].append(facolta_selezionata)
            data["Numero"].append(telefono)
            data["IDGruppi"].append(gruppo_selezionato)
    
    return pd.DataFrame(data)

# Genera il dataset con facoltà e relative informazioni
facolta_df = generate_istanza_di_corso(len(facolta))

# Scrive il DataFrame in un file CSV
output_csv = "popolamento_telefono_con_gruppiasdsda.csv"
facolta_df.to_csv(output_csv, index=False)

print(f"Dati popolati salvati nel file: {output_csv}")
