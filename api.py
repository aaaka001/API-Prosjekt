# Funksjon som henter alle valutaer fra APIen
import requests
from key import API_KEY

def get_currency():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"

    response = requests.get(url)
    data = response.json()

    if data["result"] == "success":
        codes = data["supported_codes"]
        return {code[0]: code[1] for code in codes}
    else:
        return {}


# Funksjon som konverterer
def convert_currency(base, target, amount):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base}/{target}/{amount}"

    response = requests.get(url)
    data = response.json()

    if data["result"] == "success":
        return data["conversion_result"]
    return None

