import pandas as pd

# Load the Excel file
datei = "C:\\Users\\Falk\\TestData\\Sales.xlsx"
df=pd.read_excel(datei,sheet_name="Sheet")


# filter criteria
high_sales = df[df['SalesAmount']>100]

"""
complex sample
high_sales = df[(df['SalesAmount'] > 100) & (df['SalesAmount'] < 2000)]

"""

# Display the first 5 rows of the DataFrame
print(high_sales)


# write dataframe to excel
file_path =  "C:\\Users\\Falk\\TestData\\filteredSales.xlsx"
high_sales.to_excel(file_path,index=False)

print("\nExcel file has been successfully created\n")

