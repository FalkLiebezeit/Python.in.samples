
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