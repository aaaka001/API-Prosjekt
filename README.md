# Valutakalkulator

### Hva gjør valutakalkulatoren?
  - Regner ut valutakursene til og fra alle tilgjengelige valutakurs
  - Lagrer konverteringene dine i en txt som lages automatisk

### Funksjoner
  - Henter alle tilgjengelige valutaer fra API
  - Lagrer konverteringer i en txt
  - Konverterer mellom to valgfrie valutaer
  - Viser både valutakode og fullt navn
  - Unngår unødvendige API kall
  - Feilhåndtering for
    -  Ugyldig tall
    -  Ugyldig valutakode
    -  Samme valuta valgt
    -  API-feil

### Teknologier brukt
  - Python
  - Tkinter (GUI Rammeverk)
  - Tkinter ttk (Moderne widgets)
  - Datetime (Dato, tid)
  - requests (HTTP-kall)
  - ExchangeRate-API (https://www.exchangerate-api.com/)
  - Git (Versjonskontroll)

### Hvordan kjøre programmet
  1. Klon repositorien med git, eller nedlast repositorien
  2. Lag en ny fil som heter key.py og lag en variabel som heter API_KEY og sett inn API nøkkelen din.
  3. Lag en virtual environment og installer requests ved å gjøre det følgende i terminalen:
      - python3 -m venv .venv
      - source .venv/bin/activate
      - pip install requests
  5. Kjør koden ved å skrive "python main.py" i terminalen.

### Starter ikke programmet? Sjekk at:

  - Du har installert python3
  - Du har installert requests
  - Du har laget key.py med gyldig API_KEY

### Får ugyldig valutakode

  - Skriv valutakoden med STORE bokstaver
  - Velg valuta i dropdown menyen

## Prosjektstruktur

- main.py – GUI og brukerinteraksjon
- api.py – API-kall og logikk
- key.py – API-nøkkel (ikke inkludert i repo)



