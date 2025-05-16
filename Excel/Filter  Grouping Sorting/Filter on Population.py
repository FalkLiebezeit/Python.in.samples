import pandas as pd

# Load the Excel file
datei = "C:\\Users\\Falk\\TestData\\CountriesCapitalsPopulations.xlsx"
df=pd.read_excel(datei,sheet_name="Tabelle1")


# filter criteria
high_population = df[(df['Population'] > 100000000) & (df['Population'] < 200000000)]


# Display the first 5 rows of the DataFrame
print("\n\nResult :\n\n")
print(high_population)


# write dataframe to excel
file_path =  "C:\\Users\\Falk\\TestData\\CountriesCapitalsPopulations_FilteredOnPopulation.xlsx"
high_population.to_excel(file_path,index=False)

print("\n\nExcel file has been successfully created\n")

