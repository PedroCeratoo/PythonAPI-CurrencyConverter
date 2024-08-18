import xmltodict

with open("currency.xml", "rb") as currency_file:
    dic_currency = xmltodict.parse(currency_file)

