import xmltodict


def currency_name():
    with open("currency.xml", "rb") as currency_file:
        dic_currency = xmltodict.parse(currency_file)
    coins = dic_currency["xml"]
    return coins

def available_converts():
    with open("converts.xml", "rb") as convert_file:
        dic_converts = xmltodict.parse(convert_file)

    converts = dic_converts["xml"]
    dic_available_converts = {}
    for even_convert in converts:
        origin_currency, target_currency = even_convert.split("-")
        if origin_currency in dic_available_converts:
            dic_available_converts[origin_currency].append(target_currency)
        else:
            dic_available_converts[origin_currency] = [target_currency]
    return dic_available_converts

available_converts()