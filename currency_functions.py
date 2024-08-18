import customtkinter

from pick_quot import pick_currency_quotation

def currency_convert(origin_currency_fields, target_currency_fields, text_currency_convert):
    origin_currency = origin_currency_fields.get()
    target_currency = target_currency_fields.get()

    if origin_currency and target_currency:
        quot = pick_currency_quotation(origin_currency, target_currency)
        text_currency_convert.configure(text=f"1 {origin_currency} = {quot} {target_currency}")

def for_currency_list(available_currency, currency_list):
    for index_currency, currency_code in available_currency.items():
        text_currency_list = customtkinter.CTkLabel(currency_list, text=f"{index_currency}: {currency_code}")
        text_currency_list.pack()

def target_currency_load(currency_selected, dic_converts_available, target_currency_fields):
    origin_currency_list = dic_converts_available[currency_selected]
    target_currency_fields.configure(values=origin_currency_list)
    target_currency_fields.set(origin_currency_list[0])
