import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

def ottieni_lista_artisti():
    """Recupera tutti gli artisti e i loro URL dai menu a tendina di Serebii."""
    url_index = "https://www.serebii.net/card/dex/artist/"
    print("Recupero il database degli artisti da Serebii...")
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url_index, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"Errore di connessione: {e}")
        return {}
    soup = BeautifulSoup(response.text, 'html.parser')
    artisti = {}
    for select in soup.find_all('select'):
        for option in select.find_all('option'):
            nome_visibile = option.text.strip()
            link = option.get('value')
            
            if link and link.endswith('.shtml'):
                artisti[nome_visibile] = link         
    return artisti
def scrape_serebii_cards(artist_name, artist_link):
    """Estrae le carte dato il nome e il link esatto dell'artista."""
    url = urljoin("https://www.serebii.net/card/dex/artist/", artist_link)
    print(f"\nScaricando dati per '{artist_name}' da: {url} ...")
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"Errore di connessione: {e}")
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    dati_carte = []
    for row in soup.find_all('tr'):
        if row.find_parent('td'):
            continue      
        if row.find('select'):
            continue 
        cols = row.find_all(['td', 'th'], recursive=False)
        if len(cols) >= 3:
            card_name = cols[1].get_text(separator=" ", strip=True)
            if "Card Name" in card_name or not card_name:
                continue
            set_parts = list(cols[2].stripped_strings)
            set_details = set_parts[0] if len(set_parts) > 0 else ""
            numero = " ".join(set_parts[1:]) if len(set_parts) > 1 else ""
            dati_carte.append({
                "Nome Carta": card_name,
                "Numero": numero,
                "Espansione": set_details,
            })
    if not dati_carte:
        print("Nessuna carta trovata. Verifica la struttura della pagina.")
        return
    nome_file = f"Carte_{artist_name.replace(' ', '_').replace('/', '-')}.xlsx"
    df = pd.DataFrame(dati_carte)
    df.to_excel(nome_file, index=False)
    
    print(f"Lavoro completato! Trovate {len(dati_carte)} carte.")
    print(f"File salvato con successo: {nome_file}")
if __name__ == "__main__":
    artisti_disponibili = ottieni_lista_artisti()
    if not artisti_disponibili:
        print("Impossibile caricare la lista degli artisti. Esco.")
    else:
        query = input("\nInserisci una parte del nome dell'autore (es. 'sow', 'arita', 'ken'): ").strip().lower()
        risultati = {nome: link for nome, link in artisti_disponibili.items() if query in nome.lower()}
        if not risultati:
            print("Nessun artista trovato con quel nome.")
        elif len(risultati) == 1:
            nome_esatto = list(risultati.keys())[0]
            link_esatto = list(risultati.values())[0]
            scrape_serebii_cards(nome_esatto, link_esatto)
        else:
            print("\nHo trovato più artisti che corrispondono alla tua ricerca:")
            lista_nomi = list(risultati.keys())
            for i, nome in enumerate(lista_nomi):
                print(f"{i + 1}) {nome}") 
            scelta = input("\nDigita il numero dell'artista corretto: ")
            try:
                indice = int(scelta) - 1
                if 0 <= indice < len(lista_nomi):
                    nome_esatto = lista_nomi[indice]
                    link_esatto = risultati[nome_esatto]
                    scrape_serebii_cards(nome_esatto, link_esatto)
                else:
                    print("Numero non presente in lista.")
            except ValueError:
                print("Devi inserire un numero valido.")