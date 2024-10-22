from vinted_scraper import VintedScraper


def main():
    scraper = VintedScraper("https://www.vinted.com")  # inizializza lo scraper con la baseurl
    params = {
        "search_text": "char",
        "page" : 1
        # Puoi aggiungere altri parametri di ricerca come la paginazione, ecc.
    }
    
    # Effettua la ricerca
    items = scraper.search(params)  # Ottieni tutti gli oggetti
    # Controlla se ci sono risultati
    count = 0
    if items:
        # Stampa ogni oggetto
        for item in items:
            count += 1
            print(f"Item ID: {item.id}, Title: {item.title}, Price: {item.price}, Item url: {item.url}, Image url: {item.photo.url}")
        
        # Ottieni e stampa informazioni aggiuntive su un singolo oggetto (prendiamo il primo)
        first_item = items[0]
        item_details = scraper.item(first_item.id)  # Ottieni più informazioni su un particolare oggetto
    else:
        print("No items found.")
    print(count)
if __name__ == "__main__":
    main()