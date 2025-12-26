# pip install pandas
# pip install openpyxl

import pandas as pd
import os
from datetime import datetime

# --- Display current date and time ---
print("Local current date & time:", datetime.now().strftime("%a %b %d %H:%M:%S %Y"))
print("Local current date:", datetime.today().date())

# --- Sample data for the Excel file ---
data = {
    'Name': ['John', 'Anne', 'Mike', 'Peter', 'Falk'],
    'Age': [56, 34, 54, 45, 55],  # Store ages as integers for better data handling
    'City': ['Berlin', 'NYC', 'LA', 'Bern', 'Leipzig']
}

# --- Create a pandas DataFrame from the sample data ---
df = pd.DataFrame(data)

# --- Prepare output directory and file path ---
output_dir = "./DataOutput"
os.makedirs(output_dir, exist_ok=True)  # Create OutputData folder if it does not exist

today_str = datetime.today().strftime("%Y-%m-%d")
file_name = f"Create XLSX File {today_str}.xlsx"
file_path = os.path.join(output_dir, file_name)

# --- Write the DataFrame to an Excel file ---
df.to_excel(file_path, index=False)

print(f"Excel file has been successfully created: {file_path}\n")