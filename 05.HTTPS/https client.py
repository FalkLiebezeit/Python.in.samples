"""HTTPS Client Example - Stock Price Fetcher

This module demonstrates how to fetch data from a REST API and export to Excel.
Uses a real financial API (Alpha Vantage) to get stock prices.
Falls back to openpyxl for Excel writing on systems without Excel installed.
"""

import pandas as pd
import requests
import logging
from typing import List, Dict
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Free API key for demo purposes (limited to 5 requests per minute)
# Get your own key at: https://www.alphavantage.co/support/#api-key
API_KEY = "demo"
BASE_URL = "https://www.alphavantage.co/query"


def fetch_stock_prices(symbols: List[str]) -> pd.DataFrame:
    """Fetch current stock prices from Alpha Vantage API.
    
    Args:
        symbols: List of stock symbols (e.g., ["AAPL", "GOOGL"])
        
    Returns:
        DataFrame with Symbol and Price columns
    """
    data = []
    
    for symbol in symbols:
        try:
            logging.info(f"Fetching data for {symbol}...")
            
            # Alpha Vantage API endpoint for global quote
            params = {
                "function": "GLOBAL_QUOTE",
                "symbol": symbol,
                "apikey": API_KEY
            }
            
            response = requests.get(BASE_URL, params=params, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                
                # Check if we got valid data
                if "Global Quote" in result and result["Global Quote"]:
                    quote = result["Global Quote"]
                    price = float(quote.get("05. price", 0))
                    change_percent = quote.get("10. change percent", "N/A")
                    
                    data.append({
                        "Symbol": symbol,
                        "Price": f"${price:.2f}",
                        "Change %": change_percent
                    })
                    logging.info(f"✓ {symbol}: ${price:.2f}")
                else:
                    logging.warning(f"No data available for {symbol}")
                    data.append({
                        "Symbol": symbol,
                        "Price": "N/A",
                        "Change %": "N/A"
                    })
            else:
                logging.error(f"HTTP Error {response.status_code} for {symbol}")
                data.append({
                    "Symbol": symbol,
                    "Price": "Error",
                    "Change %": "N/A"
                })
                
        except requests.RequestException as e:
            logging.error(f"Request failed for {symbol}: {e}")
            data.append({
                "Symbol": symbol,
                "Price": "Error",
                "Change %": "N/A"
            })
        except Exception as e:
            logging.error(f"Unexpected error for {symbol}: {e}")
            data.append({
                "Symbol": symbol,
                "Price": "Error",
                "Change %": "N/A"
            })
    
    return pd.DataFrame(data)


def save_to_excel_openpyxl(df: pd.DataFrame, filename: str) -> bool:
    """Save DataFrame to Excel using openpyxl (cross-platform).
    
    Args:
        df: DataFrame to save
        filename: Output filename
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Use openpyxl engine for better compatibility
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Stock Prices')
            
            # Get workbook and worksheet
            workbook = writer.book
            worksheet = writer.sheets['Stock Prices']
            
            # Format header row
            for cell in worksheet[1]:
                cell.font = cell.font.copy(bold=True)
            
            # Auto-adjust column widths
            for column in worksheet.columns:
                max_length = 0
                column_letter = column[0].column_letter
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = min(max_length + 2, 50)
                worksheet.column_dimensions[column_letter].width = adjusted_width
        
        logging.info(f"✓ Excel file saved successfully: {filename}")
        return True
        
    except Exception as e:
        logging.error(f"Failed to save Excel file: {e}")
        return False


def main():
    """Main function to fetch stock data and save to Excel."""
    # List of stock symbols to fetch
    stocks = ["IBM", "MSFT"]  # Using demo API, limited symbols work
    
    print("=" * 60)
    print("Stock Price Fetcher")
    print("=" * 60)
    print(f"Fetching data for: {', '.join(stocks)}")
    print("Note: Using demo API key (limited functionality)")
    print("=" * 60 + "\n")
    
    # Fetch stock prices
    stock_data = fetch_stock_prices(stocks)
    
    # Display the data
    print("\n" + "=" * 60)
    print("Fetched Data:")
    print("=" * 60)
    print(stock_data.to_string(index=False))
    print("=" * 60 + "\n")
    
    # Save to Excel
    filename = "stock_prices.xlsx"
    if save_to_excel_openpyxl(stock_data, filename):
        print(f"\n✓ Data successfully exported to '{filename}'")
    else:
        print(f"\n✗ Failed to export data to Excel")
        sys.exit(1)


if __name__ == "__main__":
    main()
