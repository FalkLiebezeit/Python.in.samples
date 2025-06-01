"""
Copilot:
Create a Python program. The program should generate and store 10,000 random numbers between 0 and 9.
The program should then create an Excel file and a table.
In this table, the header row should contain the numbers 0 to 9.
The first row should display the frequency of each digit in the random numbers.
Create a bar chart from these numbers in the Excel file.
Save the Excel file.

"""
import random
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

# Generate 10,000 random numbers between 0 and 9
random_numbers = [random.randint(0, 9) for _ in range(10000)]

# Count occurrences of each digit
frequency = {i: random_numbers.count(i) for i in range(10)}

# Create a DataFrame for the Excel file
df = pd.DataFrame([frequency], columns=range(10))

# Create an Excel writer object
excel_filename = "random_numbers_distribution.xlsx"
writer = pd.ExcelWriter(excel_filename, engine="openpyxl")

# Write data to Excel
df.to_excel(writer, sheet_name="Data", index=False)

# Create a bar chart
plt.figure(figsize=(8, 5))
plt.bar(frequency.keys(), frequency.values(), color="blue")
plt.xlabel("Digits")
plt.ylabel("Frequency")
plt.title("Frequency of Digits in 10,000 Random Numbers")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Save the chart as an image
chart_filename = "random_numbers_chart.png"
plt.savefig(chart_filename)

# Load workbook and insert the chart into the Excel file
wb = writer.book
ws = wb["Data"]

# Insert the chart image into the Excel file
img = openpyxl.drawing.image.Image(chart_filename)
ws.add_image(img, "A3")  # Positioning the image inside the sheet

# Save the Excel file
writer._save()

print(f"Excel file '{excel_filename}' with embedded bar chart has been created successfully.")