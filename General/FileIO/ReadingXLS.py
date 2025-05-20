# python

import pandas as pd

# Load the Excel file
#df=pd.read_excel("C:\\PythonFiles\\Knete.xlsx",sheet_name="Übersicht")
df=pd.read_excel("C:\\Users\\Falk\\OneDrive\\Dokumente\\Falk\\Knete.xlsx",sheet_name="Übersicht")

# Display the first 5 rows of the DataFrame
print(df.head())

write_data=df.to_excel("C:\\Users\\Falk\\OneDrive\\Dokumente\\_OutputFiles\\Test.xlsx",index=False)
