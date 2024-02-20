import json
import sys
import xlsxwriter

# Expecting a JSON string from the first command-line argument
data_json = sys.argv[1]

try:
    # Convert the JSON string to a Python list of dictionaries
    sssd_data = json.loads(data_json)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    sys.exit(1)

# Define the path for the Excel report file
report_file = "/root/report/ADGroup_linux_report.xlsx"

# Create a new Excel workbook and add a worksheet
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Define formatting for headers and data cells
header_format = workbook.add_format({
    'bold': True,
    'align': 'center',
    'bg_color': 'yellow',
    'border': 1
})
data_format = workbook.add_format({
    'align': 'left',
    'valign': 'top',
    'text_wrap': True,
    'border': 1
})

# Write the headers to the first row
worksheet.write('A1', 'Hostname', header_format)
worksheet.write('B1', 'AD Configuration Status', header_format)
worksheet.write('C1', 'AD Group', header_format)

# Start writing data from the second row
row = 1
for entry in sssd_data:
    # Write data into columns A, B, and C
    worksheet.write(row, 0, entry['hostname'], data_format)
    worksheet.write(row, 1, entry['status'], data_format)
    worksheet.write(row, 2, entry['values'], data_format)  # Assuming 'values' is a string
    row += 1

# Set column widths for clarity
worksheet.set_column('A:A', 20)  # Hostname
worksheet.set_column('B:B', 20)  # Status
worksheet.set_column('C:C', 50)  # Groups

# Close the workbook to save the Excel file
workbook.close()
