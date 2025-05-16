import pandas as pd

# Load the Excel file
datei = "C:\\Users\\Falk\\TestData\\CreateRows.xlsx"
df=pd.read_excel(datei,sheet_name="Sheet")

# Display the first 5 rows of the DataFrame
print(df.head())

