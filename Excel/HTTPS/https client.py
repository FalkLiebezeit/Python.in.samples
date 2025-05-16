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


        """
        try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for HTTP issues
        data = response.json()
        except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        data = None
        """
    
    return pd.DataFrame(data)


"""
enhancements

def get_stock_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get('Global Quote', {})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching stock data: {e}")
        return {}

def display_stock_data(stock_data):
    price = stock_data.get('05. price', 'N/A')
    volume = stock_data.get('06. volume', 'N/A')
    change = stock_data.get('09. change', 'N/A')
    print(f'Stock Price: {price}')
    print(f'Volume: {volume}')
    print(f'Change: {change}')

# Call functions
stock_data = get_stock_data('AAPL', API_KEY)
display_stock_data(stock_data)

logging.info(f'Stock Price: {price}')
logging.info(f'Volume: {volume}')
logging.info(f'Change: {change}')
"""

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
