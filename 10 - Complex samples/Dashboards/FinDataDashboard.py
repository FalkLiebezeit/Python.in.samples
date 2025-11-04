import pandas as pd

# Load the CSV file 'FinDataII.csv' from the 'DataInput' directory
file_path = "DataInput/FinDataII.csv"
df = pd.read_csv(file_path)  # Read the CSV file into a DataFrame

# Save the DataFrame as an Excel file in the 'DataOutput' directory
output_path = "DataOutput/FinDataII.xlsx"
df.to_excel(output_path, index=False)  # Write DataFrame to Excel without row indices

# Confirm successful save with a message
print(f"File saved as {output_path}")