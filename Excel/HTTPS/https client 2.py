
#URL : https://medium.com/design-bootcamp/a-stock-market-api-example-315085314270

import requests

# Set your API key and stock symbol
API_KEY = 'your_api_key'
symbol = 'AAPL'  # Apple stock symbol

# API endpoint URL
url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'

# Send a GET request to the API
response = requests.get(url)

# Parse the response JSON
data = response.json()

# Extract the relevant stock data with error handling
if 'Global Quote' in data and data['Global Quote']:
    price = data['Global Quote'].get('05. price', 'N/A')
    volume = data['Global Quote'].get('06. volume', 'N/A')
    change = data['Global Quote'].get('09. change', 'N/A')

    # Print the data
    print(f'Stock Price: {price}')
    print(f'Volume: {volume}')
    print(f'Change: {change}')
else:
    print("Error: Unable to retrieve stock data.")


"""
import pandas as pd
import xlwings as xw
import requests  # Missing import

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


"""
