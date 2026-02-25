import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Nøkkelen
API_KEY = "f587254324a3b6f5f6559cbf"


root = tk.Tk() #Lager main framen
root.title("Valutakalkulator") 

currencies = ["NOK", "USD", "EUR", "SEK", "GBP", "DKK"]

# Beløp å konvertere fra
amount_label = tk.Label(root, text="Skriv inn beløp:")
amount_label.grid(row=0, column=0)

amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

# valuta å konvertere fra
from_label = tk.Label(root, text = "Velg valuta å konvertere fra: ")
from_label.grid(row = 1, column = 0)

from_currency = ttk.Combobox(root, values=currencies, state="readonly")
from_currency.grid(row=1, column=1)
from_currency.current(0)

# valuta å konvertere til
to_label = tk.Label(root, text="Velg valuta å konvertere til: ")
to_label.grid(row=2, column=0)

to_currency = ttk.Combobox(root, values = currencies, state="readonly")
to_currency.grid(row=2, column=1)
to_currency.current(1)

# Resultatet du får!!
result_label = tk.Label(root, text="",)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Funksjon som konverterer
def conversion():
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Feil", "Skriv inn et gyldig tall.")
        return

    base = from_currency.get()
    target = to_currency.get()

    if base == target:
        messagebox.showwarning("Ugyldig valg", "Velg to forskjellige valutaer.")
        return
    
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}"

    try:
        response = requests.get(url)
        data = response.json()

        rate = data["conversion_rates"][target]
        result = amount * rate

        result_label.config(text=f"{amount} {base} = {result:.2f} {target}")
    except:
        messagebox.showerror("Feil", "Kunne ikke hente valutakurs...")


convert_button = tk.Button(root, text="Konverter", command=conversion)
convert_button.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()