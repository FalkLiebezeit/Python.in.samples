"""
Copilot:
Create an Excel spreadsheet. 
List all the countries of the world in the first column, their capitals in the second column and their
population in the third column.

"""

from openpyxl import Workbook

# Create a new workbook and sheet
wb = Workbook()
sheet = wb.active
sheet.title = "Countries Data"

# Add headers
sheet.append(["Country", "Capital", "Population"])

# List of countries, capitals, and populations (sample data)
countries_data = [
    ["China", "Beijing", 1412600000],
    ["India", "New Delhi", 1407600000],
    ["United States", "Washington, D.C.", 331900000],
    ["Indonesia", "Jakarta", 277500000],
    ["Pakistan", "Islamabad", 240500000],
    ["Brazil", "Brasilia", 216400000],
    ["Nigeria", "Abuja", 223800000],
    ["Bangladesh", "Dhaka", 172900000],
    ["Russia", "Moscow", 143400000],
    ["Mexico", "Mexico City", 128500000],
    ["Japan", "Tokyo", 125700000],
    ["Ethiopia", "Addis Ababa", 126500000],
    ["Philippines", "Manila", 117300000],
    ["Egypt", "Cairo", 113500000],
    ["Vietnam", "Hanoi", 100800000],
    ["Germany", "Berlin", 84000000],
    ["Turkey", "Ankara", 86000000],
    ["France", "Paris", 68000000],
    ["United Kingdom", "London", 67000000],
    ["Italy", "Rome", 59000000]
]

# Add all countries to the Excel sheet
for country, capital, population in countries_data:
    sheet.append([country, capital, population])

# Save the workbook
wb.save("Countries_Capitals_Populations.xlsx")
print("Excel file created successfully!")