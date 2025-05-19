# pip install pandas
# pip install openpyxl

import pandas as pd
import os


import time;
from datetime import datetime


# get date and time
localtime = time.asctime(time.localtime(time.time()))

print("Local current date & time :",localtime)
print("Local current date :", datetime.today().date())


# sample data

data = {

    'Name' : [ 'John', 'Anne', 'Mike','Peter','Falk'],
    'Age' : [ '56', '34', '54','45','55'],
    'City' :  [ 'Berlin', 'NYC', 'LA','Bern','Leipzig']
}

# create pandas dataframe
df = pd.DataFrame(data)

today =  str(datetime.today().date())

# define file path
#fileDate = " ".join(["C:\\Users\\Falk\\TestData\\XLScreated", today])
#fileDateTime = " ".join(["C:\\Users\\Falk\\TestData\\XLScreated", localtime])

fileDate = " ".join([".\\Excel\\FileIO\\Create XLSX File", today])
#fileDateTime = " ".join([".\\Excel\\FileIO\\Create XLSX File", localtime])



file_path = " ".join([fileDate, ".xlsx"])



# write dataframe to excel
df.to_excel(file_path,index=False)

print("Excel file has been successfully created\n")