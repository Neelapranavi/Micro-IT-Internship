import requests
import tkinter as tk
from tkinter import ttk, messagebox

API_KEY = 'b07506731b5faa412904a230'
URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def convert_currency():
    from_curr = from_currency.get()
    to_curr = to_currency.get()
    amount = float(amount_entry.get())

    try:
        response = requests.get(URL + from_curr)
        data = response.json()
        rate = data['conversion_rates'][to_curr]
        converted_amount = round(amount * rate, 2)
        result_label.config(text=f"{amount} {from_curr} = {converted_amount} {to_curr}")
    except Exception as e:
        messagebox.showerror("Error", "API Error or Invalid Currency Code")

# UI
window = tk.Tk()
window.title("Currency Converter")

currencies = ["USD", "INR", "EUR", "GBP", "JPY", "CAD", "AUD"]

tk.Label(window, text="From Currency").pack()
from_currency = ttk.Combobox(window, values=currencies)
from_currency.set("USD")
from_currency.pack()

tk.Label(window, text="To Currency").pack()
to_currency = ttk.Combobox(window, values=currencies)
to_currency.set("INR")
to_currency.pack()

tk.Label(window, text="Amount").pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

tk.Button(window, text="Convert", command=convert_currency).pack(pady=5)
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
