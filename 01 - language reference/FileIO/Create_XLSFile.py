# pip install pandas
# pip install openpyxl


import pandas as pd

# sample data

data = {

    'Name' : [ 'John', 'Anne', 'Mike','Peter','Falk'],
    'Age' : [ '56', '34', '54','45','55'],
    'City' :  [ 'Berlin', 'NYC', 'LA','Bern','Leipzig']
}

# create pandas dataframe
df = pd.DataFrame(data)

# define file path
file_path = './DataOutput/XLS created.xlsx'

# write dataframe to excel
df.to_excel(file_path,index=False)

print("Excel file has been successfully created")