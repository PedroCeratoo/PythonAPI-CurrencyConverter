import customtkinter
from currency_functions import currency_convert, for_currency_list, target_currency_load
from pick_currency import currency_name, available_converts

# Create and set window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("500x500")

dic_converts_available = available_converts()

# Create elements
title = customtkinter.CTkLabel(window, text="Currency Converter", font=("Montserrat", 20))
text_origin_currency = customtkinter.CTkLabel(window, text=" Select the origin currency")
text_currency_target = customtkinter.CTkLabel(window, text=" Select the target currency")

origin_currency_fields = customtkinter.CTkOptionMenu(window, values=list(dic_converts_available.keys()), command=lambda x: target_currency_load(x, dic_converts_available, target_currency_fields))
target_currency_fields = customtkinter.CTkOptionMenu(window, values=["Select the target currency"])

converter_button = customtkinter.CTkButton(window, text="Convert", command=lambda: currency_convert(origin_currency_fields, target_currency_fields, text_currency_convert))
currency_list = customtkinter.CTkScrollableFrame(window)

text_currency_convert = customtkinter.CTkLabel(window, text="")

available_currency = currency_name()

for_currency_list(available_currency, currency_list)

# Show elements
title.pack(padx=10, pady=10)
text_origin_currency.pack(padx=10, pady=10)
origin_currency_fields.pack(padx=10)
text_currency_target.pack(padx=10, pady=10)
target_currency_fields.pack(padx=10)
converter_button.pack(padx=10, pady=30)
text_currency_convert.pack(padx=10, pady=10)
currency_list.pack(padx=10)

# Run window (mainloop)
window.mainloop()
