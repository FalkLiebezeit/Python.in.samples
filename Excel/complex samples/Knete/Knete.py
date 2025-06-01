"""
Ki:

Write a Python program. The program should perform the following tasks:

- Load the Excel file Knete.xlsx from the TestData subdirectory
- Display a chart from the "Overview" worksheet
- The abscissa data is in columns A4 to A19
- The ordinate data is in columns C4 to F19

"""
import pandas as pd
import matplotlib.pyplot as plt

# Define the path to the Excel file
file_path = "./TestData/Knete.xlsx"

# Load the Excel file
df = pd.read_excel(file_path, sheet_name="Overview", engine="openpyxl")

# Extract data
x_data = df.iloc[3:19, 0]  # Column A (Rows 4-19)
y_data = df.iloc[3:19, 2:6]  # Columns C-F (Rows 4-19)

# Create a line chart
plt.figure(figsize=(10, 6))

# Plot each column from C to F
for col in y_data.columns:
    plt.plot(x_data, y_data[col], marker='o', label=df.columns[col])
     #plt.plot(x_data, y_data[col], marker='o', label=df.columns[0])
# Customize chart
plt.xlabel("Abscissa Data (Column A)")
plt.ylabel("Ordinate Data (Columns C-F)")
plt.title("Chart from Overview Worksheet")
plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.legend()  # Show legend with column names
plt.grid(True, linestyle="--", alpha=0.7)

# Display the chart
plt.show()