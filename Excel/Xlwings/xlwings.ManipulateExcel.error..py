#Xlwings Script
import xlwings as xw

#Connect to Excel
wb = xw.Book('C:\\Users\\Falk\\TestData\\Knete.xlsx') 
sheet =wb.sheets['Übersicht']

#Read values from Excel
data = sheet.range('A1:A19').value

#Perform some computations
data_squared = [x*x for x in data]

#Write results back to Excel 
sheet.range('A30:A39').value = data_squared

#Close the workbook
wb.save()
wb.close()

