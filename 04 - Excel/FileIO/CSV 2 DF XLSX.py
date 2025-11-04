import pandas as pd
import os

# --- Ensure OutputData directory exists ---
output_dir = "./DataOutput"
os.makedirs(output_dir, exist_ok=True)

# --- Display current working directory ---
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# --- Path to the input CSV file ---
#csv_path = './Excel/FileIO/FFB.csv'
csv_path = './DataInput/FFB.csv'
# --- Read the CSV file directly into a DataFrame ---
try:
    df = pd.read_csv(csv_path)
    print("CSV file loaded successfully.")
except Exception as e:
    print(f"Error loading CSV file: {e}")
    df = pd.DataFrame()  # Empty DataFrame as fallback

# --- Save the DataFrame to CSV and Excel formats in OutputData ---
csv_output = os.path.join(output_dir, "CSV 2 DF XLSX.csv")
xlsx_output = os.path.join(output_dir, "CSV 2 DF XLSX.xlsx")

df.to_csv(csv_output, index=False)
df.to_excel(xlsx_output, index=False)

# --- Show the first and last few rows of the DataFrame ---
print("\nLast rows of DataFrame:")
print(df.tail())
print("\nFirst rows of DataFrame:")
print(df.head())