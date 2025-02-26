-- Creazione della tabella Corso
CREATE TABLE Corso (
    Codice INT PRIMARY KEY CHECK (Codice >= 1000 AND Codice <= 9999),
    Nome VARCHAR(100) NOT NULL,
    Durata INT NOT NULL CHECK (Durata > 0 AND Durata <= 12),
    Descrizione TEXT,
    NModuli INT NOT NULL CHECK (NModuli = 1 OR NModuli = 2),
);

-- Creazione della tabella Esame
CREATE TABLE Esame (
    Nome VARCHAR(100) PRIMARY KEY,
    NCrediti INT NOT NULL CHECK (NCrediti > 0 AND NCrediti <= 24),
);

-- Creazione della tabella Facoltà
CREATE TABLE Facoltà (
    Nome VARCHAR(100) PRIMARY KEY,
    Telefono VARCHAR(20) UNIQUE NOT NULL CHECK (LENGTH(Telefono) => 10),
    Sede VARCHAR(100) UNIQUE NOT NULL
);


-- Creazione della tabella Telefono
CREATE TABLE Telefono (
    NomeFacoltà VARCHAR(100),
    Numero VARCHAR(20) UNIQUE NOT NULL CHECK (LENGTH(Numero) => 10),
    PRIMARY KEY (NomeFacoltà, Numero),
    FOREIGN KEY (NomeFacoltà) REFERENCES Facoltà(Nome) ON UPDATE CASCADE
);

-- Creazione della tabella Sede
CREATE TABLE Sede (
    NomeFacoltà VARCHAR(100),
    Sede VARCHAR(100) UNIQUE NOT NULL,
    PRIMARY KEY (NomeFacoltà, Sede),
    FOREIGN KEY (NomeFacoltà) REFERENCES Facoltà(Nome) ON UPDATE CASCADE
);

-- Creazione della tabella CorsoDiLaurea
CREATE TABLE CorsoDiLaurea (
    Nome VARCHAR(100) PRIMARY KEY,
    NomeFacoltà VARCHAR(100) NOT NULL,
    FOREIGN KEY (NomeFacoltà) REFERENCES Facoltà(Nome) ON UPDATE CASCADE
);

-- Creazione della tabella Orientamento
CREATE TABLE Orientamento (
    Nome VARCHAR(100) PRIMARY KEY,
    PianoDiStudio VARCHAR(100) NOT NULL,
    NStudenti INT NOT NULL CHECK (NStudenti > 0),
    NomeCDL VARCHAR(100) NOT NULL,
    FOREIGN KEY (NomeCDL) REFERENCES CorsoDiLaurea(Nome) ON UPDATE CASCADE
);

-- Creazione della tabella Studente
CREATE TABLE Studente (
    Matricola INT PRIMARY KEY CHECK (Matricola > 1000000 AND Matricola < 9999999),
    Nome VARCHAR(100) NOT NULL,
    Indirizzo VARCHAR(200),
    AnnoImmatricolazione YEAR NOT NULL CHECK (AnnoImmatricolazione > 2010 AND AnnoImmatricolazione < 2025),
    Status VARCHAR(50) CHECK (Status = 'Attivo' OR Status = 'Inattivo' OR Status = 'Sospeso'),
    NomeOrientamento VARCHAR(100) NOT NULL,
    FOREIGN KEY (NomeOrientamento) REFERENCES Orientamento(Nome)
);

-- Creazione della tabella Sostiene
CREATE TABLE Sostiene (
    Nome VARCHAR(100),
    Matricola INT CHECK (Matricola > 1000000 AND Matricola < 9999999),
    PRIMARY KEY (Nome, Matricola),
    FOREIGN KEY (Nome) REFERENCES Esame(Nome), 
    FOREIGN KEY (Matricola) REFERENCES Studente(Matricola) ON UPDATE CASCADE
);

-- Creazione della tabella FaParteDi
CREATE TABLE FaParteDi (
    NomeEsame VARCHAR(100),
    NomeOrientamento VARCHAR(100),
    PRIMARY KEY (NomeEsame, NomeOrientamento),
    FOREIGN KEY (NomeEsame) REFERENCES Esame(Nome) ON UPDATE CASCADE,
    FOREIGN KEY (NomeOrientamento) REFERENCES Orientamento(Nome) ON UPDATE CASCADE
);

-- Creazione della tabella Strutturato
CREATE TABLE Strutturato (
    NomeCDL VARCHAR(100) NOT NULL,
    Codice INT NOT NULL CHECK (Codice >= 1000 AND Codice <= 9999),
    PRIMARY KEY (NomeCDL, Codice),
    FOREIGN KEY (NomeCDL) REFERENCES CorsoDiLaurea(Nome) ON UPDATE CASCADE,
    FOREIGN KEY (Codice) REFERENCES Corso(Codice) ON UPDATE CASCADE
);

-- Creazione della tabella IstanzaDiCorso
CREATE TABLE IstanzaDiCorso (
    CodiceCorso INT NOT NULL CHECK (Codice >= 1000 AND Codice <= 9999),
    Numero INT CHECK (Numero > 0),
    Anno YEAR CHECK (Anno > 2010 AND Anno < 2025),
    Semestre INT NOT NULL CHECK (Semestre = 1 OR Semestre = 2),
    Aula VARCHAR(50),
    Giorni VARCHAR(200),
    Iscritti INT CHECK (Iscritti >= 10 AND Iscritti <= 200),
    Tipo VARCHAR(50) CHECK (Tipo = 'Teoria' OR Tipo = 'Esercitazione' OR Tipo = 'Laboratorio'),
    NomeFacoltà VARCHAR(100),
    PRIMARY KEY (CodiceCorso, Numero, Anno),
    FOREIGN KEY (CodiceCorso) REFERENCES Corso(Codice) ON UPDATE CASCADE,
    FOREIGN KEY (NomeFacoltà) REFERENCES Facoltà(Nome) ON UPDATE CASCADE
);

-- Creazione della tabella Docente
CREATE TABLE Docente (
    Nome VARCHAR(100),
    Cognome VARCHAR(100),
    Ufficio VARCHAR(50),
    Telefono VARCHAR(20) CHECK (LENGTH(Telefono) => 10),
    E_mail VARCHAR(100),
    Tipo VARCHAR(50) CHECK (Tipo = 'Ricercatore' OR Tipo = 'Ordinario' OR Tipo = 'A Contratto' OR Tipo = 'Associato'),
    NomeFacoltà VARCHAR(100),
    PRIMARY KEY (Nome, Cognome),
    FOREIGN KEY (NomeFacoltà) REFERENCES Facoltà(Nome) ON UPDATE CASCADE
);

-- Creazione della tabella Tiene
CREATE TABLE Tiene (
    NomeDocente VARCHAR(100),
    CognomeDocente VARCHAR(100),
    CodiceCorso INT NOT NULL CHECK (Codice >= 1000 AND Codice <= 9999),
    NumeroCorso INT CHECK (Numero > 0),
    AnnoCorso YEAR CHECK (Anno > 2010 AND Anno < 2025),
    PRIMARY KEY (NomeDocente, CognomeDocente, CodiceCorso, NumeroCorso, AnnoCorso),
    FOREIGN KEY (NomeDocente, CognomeDocente) REFERENCES Docente(Nome, Cognome) ON UPDATE CASCADE,
    FOREIGN KEY (CodiceCorso) REFERENCES Corso(Codice) ON UPDATE CASCADE,
    FOREIGN KEY (NumeroCorso, AnnoCorso) REFERENCES IstanzaDiCorso(Numero, Anno) ON UPDATE CASCADE
);
