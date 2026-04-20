import tkinter as tk
from tkinter import ttk, messagebox # ttk
from key import API_KEY # Henter API_KEY variabelen fra key.py
from api import get_currency, convert_currency # Henter funksjonene fra api.py
from datetime import datetime #Datetime for å hente tid for logg

# Funksjon som viser resultat fra convert_currency!
def conversion():
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Feil", "Skriv inn et gyldig tall.")
        return

    #hente valutakode
    base = from_currency.get().split(" - ")[0]
    target = to_currency.get().split(" - ")[0]

    # Sjekker base og target 
    if base not in currency_dict:
        messagebox.showerror("Feil", f"{base} er ikke en gyldig valuta")
        return
    
    if target not in currency_dict:
        messagebox.showerror("Feil", f"{target} er ikke en gyldig valuta")
        return

    # Unngå unødvendig api kall ved unødvendig konversjoner
    if base == target:
        messagebox.showwarning("Ugyldig valg", "Velg to forskjellige valutaer.")
        return

    result = convert_currency(base, target, amount) # Sender koden til api

    # Feilhåndterer api kall. Sjekker om den fant resultat eller ikke
    if result is None:
        messagebox.showerror("Feil", "Kunne ikke hente valutakurs.")
    else:
        result_label.config(text=f"{amount} {base} = {result:.2f} {target}")
        save_log(amount, base, target, result)

# Funksjon for å lage txt fil, skrive og lagre. 
def save_log(amount, base, target, result):
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    log_line = f"{now} | {amount} {base} -> {result:.2f} {target}\n"
    
    with open("oversettelse_logg.txt", "a", encoding="utf-8") as file:
        file.write(log_line)

root = tk.Tk() #Lager main framen
root.title("Valutakalkulator")

# Henter valutaer fra api.py
currency_dict = get_currency()
if not currency_dict: # Sjekker om API'en hentet data
    messagebox.showerror("API Feil", "Kunne ikke hente valutaer.")
    root.destroy()


currencies = [f"{code} - {name}" for code, name in currency_dict.items()] #Lager en liste med kode og navn

# Beløp å konvertere fra
amount_label = tk.Label(root, text="Skriv inn beløp: ")
amount_label.grid(row=0, column=0)

amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

# valuta å konvertere fra
from_label = tk.Label(root, text = "Velg valuta å konvertere fra: ")
from_label.grid(row = 1, column = 0)

from_currency = ttk.Combobox(root, values=currencies)
from_currency.grid(row=1, column=1)
from_currency.current(0)

# valuta å konvertere til
to_label = tk.Label(root, text="Velg valuta å konvertere til: ")
to_label.grid(row=2, column=0)

to_currency = ttk.Combobox(root, values=currencies)
to_currency.grid(row=2, column=1)
to_currency.current(1)

#OBS
obs = tk.Label(root, text="Bruk STORE bokstaver når du SKRIVER inn valutakurs. (Caps on)")
obs.grid(row=5, column=0)

# Resultatet du får!!
result_label = tk.Label(root, text="",)
result_label.grid(row=4, column=0, columnspan=2, pady=10)


convert_button = tk.Button(root, text="Konverter", command=conversion)
convert_button.grid(row=3, column=0, columnspan=2, pady=5)

    
root.mainloop()