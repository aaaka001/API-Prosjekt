- Funksjoner
  - Henter alle tilgjengelige valutaer fra API
  - Konverterer mellom to valgfrie valutaer
  - Viser både valutakode og fullt navn
  - Unngår unødvendig API kall
  - Debugging for
    -  Ugyldig tall
    -  Ugyldig valutakode
    -  Samme valuta valgt
    -  API-feil

- Teknologier brukt
  - Python
  - Tkinter (GUI Rammeverk)
  - Tkinter ttk (Moderne widgets)
  - requests (HTTP-kall)
  - ExchangeRate-API (https://www.exchangerate-api.com/

- Hvordan kjøre programmet
  1. Klon repositorien med git, eller nedlast repositorien
  2. Lag en ny fil som heter key.py og lag en variabel som heter API_KEY og sett inn API nøkkelen din.
  3. Lag en virtual environment og installer requests ved å gjøre det følgende i terminalen:
    - python3 -m venv .venv
    - source .venv/bin/activate
    - pip install requests
  5. Kjør koden ved å skrive "python main.py" i terminalen.














