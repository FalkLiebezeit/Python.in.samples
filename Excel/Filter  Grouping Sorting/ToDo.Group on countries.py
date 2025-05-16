import pandas as pd

# Load the Excel file
datei = "C:\\Users\\Falk\\TestData\\CountriesCapitalsPopulations.xlsx"
df=pd.read_excel(datei,sheet_name="Tabelle1")


#ToDo

timezone = df

"""
# Group by 'Name' and calculate the mean Score
timezone = df.groupby('TimeZone').agg({'Score': 'count'})

"""



# Display the first 5 rows of the DataFrame
print("\n\nResult :\n\n")
print(timezone)


# write dataframe to excel
file_path =  "C:\\Users\\Falk\\TestData\\CountriesCapitalsPopulations_grouped.xlsx"
timezone.to_excel(file_path,index=False)

print("\n\nExcel file has been successfully created\n")

