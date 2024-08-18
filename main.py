from locale import currency

import customtkinter

def currency_convert():
    print("Convert currency")

def for_currency_list(index, arr):
    for currency in available_currency:
        text_currency_list = customtkinter.CTkLabel(currency_list, text=currency)
        text_currency_list.pack()


#create and set window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("500x500")

#create elements

title = customtkinter.CTkLabel(window, text="Currency Converter", font=("Montserrat", 20))
text_origin_currency = customtkinter.CTkLabel(window, text=" Select the origin currency")
text_currency_target = customtkinter.CTkLabel(window, text=" Select the target currency")

origin_currency_fields = customtkinter.CTkOptionMenu(window, values=["USD", "BRL", "EUR", "BTC"])
target_currency_fields = customtkinter.CTkOptionMenu(window, values=["USD", "BRL", "EUR", "BTC"])

converter_button = customtkinter.CTkButton(window, text="Convert", command=currency_convert)
currency_list = customtkinter.CTkScrollableFrame(window)

available_currency = ["USD: American Dollar", "BRL: Brazillian Real", "BTC: Bitcoin"]

for_currency_list(currency, available_currency)


#show elements

title.pack(padx=10, pady=10)
text_origin_currency.pack(padx=10, pady=10)
origin_currency_fields.pack(padx=10)
text_currency_target.pack(padx=10, pady=10)
target_currency_fields.pack(padx=10)
converter_button.pack(padx=10, pady=30)
currency_list.pack(padx=10)



#run window (mainloop)
window.mainloop()