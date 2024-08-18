import requests

def pick_currency_quotation(origin_currency, target_currency):
    link = f"https://economia.awesomeapi.com.br/last/{origin_currency}-{target_currency}"
    request = requests.get(link)
    quotation = (request.json()[f"{origin_currency}{target_currency}"]["bid"])
    return quotation

