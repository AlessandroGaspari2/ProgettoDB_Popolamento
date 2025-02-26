import pandas as pd
from faker import Faker
import random

# Instanzio Faker
faker = Faker()

# Carica il CSV dei dati delle facoltà
facoltà_csv = "popolamentoBD\csv\popolamento_facolta.csv"  # Percorso corretto del tuo file CSV
df_facoltà = pd.read_csv(facoltà_csv)
facoltà = df_facoltà.iloc[:, 0].tolist()  # Ottieni i nomi delle facoltà

# Funzione per generare un dataset di Docente utilizzando Faker
def generate_docenti(num):
    data = {
        "Nome": [],
        "Cognome": [],
        "Ufficio": [],
        "Telefono": [],
        "E_mail": [],
        "Tipo": [],
        "NomeFacoltà": []
    }
    
    for _ in range(num):
        # Genera dati casuali
        nome = faker.first_name()
        cognome = faker.last_name()
        ufficio = f"Uff-{random.randint(101, 200)}"  # Ufficio casuale (Uff-101 a Uff-110)
        prefisso = "+39"  # Prefisso italiano
        numero_base = random.randint(1000000000, 9999999999)  # Numero base di 10 cifre
        telefono = f"{prefisso}{numero_base}"  # Genera numero di telefono        
        email = faker.email()  # Genera indirizzo email
        tipo = random.choice(["Ricercatore", "Associato", "Ordinario", "A Contratto"])  # Tipo casuale
        facoltà_selezionata = random.choice(facoltà)  # Facoltà casuale
        
        # Aggiungi i dati al dataset
        data["Nome"].append(nome)
        data["Cognome"].append(cognome)
        data["Ufficio"].append(ufficio)
        data["Telefono"].append(telefono)
        data["E_mail"].append(email)
        data["Tipo"].append(tipo)
        data["NomeFacoltà"].append(facoltà_selezionata)

    return pd.DataFrame(data)

# Genera il dataset
docenti_df = generate_docenti(len(facoltà))

# Scrive il DataFrame in un file CSV
output_csv = "popolamento_docenti.csv"
docenti_df.to_csv(output_csv, index=False)

print(f"Dati popolati salvati nel file: {output_csv}")
