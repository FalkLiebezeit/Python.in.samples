"""
Ki:

Write a Python program. The program should perform the following tasks:

- Load the Excel file Financials.xlsx from the TestData subdirectory
- Display a chart from the "Overview" worksheet
- The abscissa data is in columns A4 to A65
- The ordinate data is in columns C4 to F65
- Use the matplotlib library to display the chart

"""
import pandas as pd
import matplotlib.pyplot as plt

# Define file and sheet
file_path = "TestData/Financials.xlsx"
sheet_name = "Overview"

try:
    # Load the worksheet into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please check the path.")
    exit()
except ValueError:
    print(f"Error: The sheet '{sheet_name}' does not exist in the file. Please verify the sheet name.")
    exit()
except Exception as e:
    print(f"Error: An unexpected error occurred: {e}")
    exit()

# Extract abscissa (A4:A65) and ordinate (C4:F65) data
x_data = df.iloc[3:65, 0]      # Rows 4-65 (0-based index 3:65), column A
y_data = df.iloc[3:65, 2:6]    # Rows 4-65, columns C-F

# Plot the data
plt.figure(figsize=(10, 5))
for column in y_data.columns:
    plt.plot(x_data, y_data[column], label=str(column))

plt.xlabel("Abscissa (A4:A65)")
plt.ylabel("Ordinate (C4:F65)")
plt.title("Chart from 'Overview' Worksheet")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()