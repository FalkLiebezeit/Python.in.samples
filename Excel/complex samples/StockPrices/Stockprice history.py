"""
Ki:

Write a Python program:

- The program loads the Excel file "Stockprice.xlsx" from the ".\TestData\" subdirectory.

- The program then saves the file in the ".\TestData\" directory.

answer: 


"""
import pandas as pd

# Define file paths
input_file = r".\TestData\Stockprices.xlsx"

output_file = r".\TestData\Stockprices_saved.xlsx"

# Load the Excel file
df = pd.read_excel(input_file)

# Save the file to the specified directory
df.to_excel(output_file, index=False)

print(f"File saved successfully to {output_file}")