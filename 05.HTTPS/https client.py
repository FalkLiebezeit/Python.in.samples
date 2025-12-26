import pandas as pd
import xlwings as xw
import requests  # Missing import
import logging

logging.basicConfig(level=logging.INFO)

def fetch_stock_prices(symbols):
    data = []
    for symbol in symbols:
        

        response = requests.get(f'https://api.example.com/stock/{symbol}')
        
        if response.status_code == 200:
            price = response.json().get('price')
            data.append({"Symbol": symbol, "Price": price})
    
    return pd.DataFrame(data)



# List of stock symbols
stocks = ["AAPL", "GOOGL", "MSFT", "AMZN"]
        
# Fetch stock prices
stock_data = fetch_stock_prices(stocks)

# Start Excel app
app = xw.App(visible=True)
workbook = app.books.add()
sheet = workbook.sheets[0]

# Write DataFrame to Excel
sheet.range("A1").value = stock_data

# Formatting and saving
sheet.range("A1:B1").font.bold = True
workbook.save("stock_prices.xlsx")
workbook.close()
app.quit()

print("Excel-Datei erfolgreich gespeichert.")
