import pandas as pd

# Load the Excel file
datei = "C:\\Users\\Falk\\TestData\\CountriesCapitalsPopulations.xlsx"
df=pd.read_excel(datei,sheet_name="Tabelle1")


# Sort by Country column in ascending order
df_sorted = df.sort_values(by='Country')

"""
df_sorted_desc = df.sort_values(by='Country', ascending=False)
"""


# Display the first 5 rows of the DataFrame
print("\n\nResult :\n\n")
print(df_sorted)


# write dataframe to excel
file_path =  "C:\\Users\\Falk\\TestData\\CountriesCapitalsPopulations_sorted on country column.xlsx"
df_sorted.to_excel(file_path,index=False)

print("\n\nExcel file has been successfully created\n")

