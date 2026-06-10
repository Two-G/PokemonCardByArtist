# PokemonCardByArtist

🇮🇹 Italiano | 🇬🇧 English

---

## 🇮🇹 Descrizione

Questo script Python permette di cercare un illustratore delle carte Pokémon sul database di Serebii e di esportare tutte le carte associate a quell'artista in un file Excel (.xlsx).

### Funzionalità

* Recupera automaticamente l'elenco completo degli artisti da Serebii.
* Permette la ricerca tramite una parte del nome dell'artista.
* Gestisce risultati multipli con una selezione interattiva.
* Estrae:

  * Nome della carta
  * Numero della carta
  * Espansione/Set
* Esporta i dati in formato Excel.

### Requisiti

Python 3.9+

Librerie necessarie:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

### Utilizzo

Avviare il programma:

```bash
python main.py
```

Inserire una parte del nome dell'artista quando richiesto:

```text
Inserisci una parte del nome dell'autore:
```

Esempi:

```text
arita
sow
ken
```

Il programma genererà un file Excel:

```text
Carte_Mitsuhiro_Arita.xlsx
```

### Struttura dei dati esportati

| Nome Carta | Numero | Espansione |
| ---------- | ------ | ---------- |
| Pikachu    | 58/102 | Base Set   |
| Charizard  | 4/102  | Base Set   |

### Disclaimer

Questo progetto utilizza dati pubblicamente disponibili su Serebii.net.

Tutti i diritti relativi ai contenuti Pokémon appartengono ai rispettivi proprietari.

---

## 🇬🇧 Description

This Python script allows users to search for a Pokémon card illustrator on the Serebii database and export all cards associated with that artist into an Excel (.xlsx) file.

### Features

* Automatically retrieves the complete artist database from Serebii.
* Supports partial artist name searches.
* Handles multiple search results with interactive selection.
* Extracts:

  * Card Name
  * Card Number
  * Expansion/Set
* Exports all data to Excel format.

### Requirements

Python 3.9+

Required libraries:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

### Usage

Run the script:

```bash
python main.py
```

Enter part of the artist's name when prompted:

```text
Enter part of the artist name:
```

Examples:

```text
arita
sow
ken
```

The script will generate an Excel file such as:

```text
Cards_Mitsuhiro_Arita.xlsx
```

### Exported Data Structure

| Card Name | Number | Expansion |
| --------- | ------ | --------- |
| Pikachu   | 58/102 | Base Set  |
| Charizard | 4/102  | Base Set  |

### Disclaimer

This project uses publicly available data from Serebii.net.

All Pokémon-related trademarks, artwork, and content belong to their respective owners.

---

## License

MIT License
