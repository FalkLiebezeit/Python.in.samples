import pandas as pd
import numpy as np
import xlsxwriter

# --- Create example data for the dashboard ---
np.random.seed(0)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': np.random.randint(1000, 5000, 12),
    'Profit': np.random.randint(200, 1000, 12),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 12)
}
df = pd.DataFrame(data)

# --- Write data to Excel with a dashboard sheet ---
with pd.ExcelWriter('./DataOutput/interactive_dashboard.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Data', index=False)
    workbook = writer.book
    worksheet = writer.sheets['Data']

    # --- Create a new worksheet for the dashboard ---
    dashboard = workbook.add_worksheet('Dashboard')

    # --- Add a title ---
    dashboard.write('A1', 'Sales Dashboard Example', workbook.add_format({'bold': True, 'font_size': 16}))

    # --- Insert a table with slicer (filter) ---
    dashboard.write('A3', 'Select Region:')
    dashboard.data_validation('B3', {'validate': 'list',
                                     'source': ['North', 'South', 'East', 'West']})

    # --- Insert a chart (Sales by Month) ---
    chart = workbook.add_chart({'type': 'column'})
    chart.add_series({
        'name': 'Sales',
        'categories': ['Data', 1, 0, 12, 0],  # Months
        'values':     ['Data', 1, 1, 12, 1],  # Sales
    })
    chart.set_title({'name': 'Monthly Sales'})
    chart.set_x_axis({'name': 'Month'})
    chart.set_y_axis({'name': 'Sales'})
    chart.set_style(10)
    dashboard.insert_chart('A5', chart, {'x_scale': 1.5, 'y_scale': 1.2})

    # --- Insert a chart (Profit by Month) ---
    chart2 = workbook.add_chart({'type': 'line'})
    chart2.add_series({
        'name': 'Profit',
        'categories': ['Data', 1, 0, 12, 0],  # Months
        'values':     ['Data', 1, 2, 12, 2],  # Profit
    })
    chart2.set_title({'name': 'Monthly Profit'})
    chart2.set_x_axis({'name': 'Month'})
    chart2.set_y_axis({'name': 'Profit'})
    chart2.set_style(12)
    dashboard.insert_chart('J5', chart2, {'x_scale': 1.5, 'y_scale': 1.2})

print("Excel dashboard 'interactive_dashboard.xlsx' created successfully.")