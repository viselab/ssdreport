import sys
import xlsxwriter
import json

# Read the JSON string from the command line argument
sssd_data_json = sys.argv[1]

try:
    # Convert the JSON string to a Python list of dictionaries
    sssd_data = json.loads(sssd_data_json)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    sys.exit(1)

# Define the Excel report file path
report_file = "/root/report/ADGroup_linux_report.xlsx"

# Create a new Excel file and add a worksheet
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Define formatting for headers and data
header_format = workbook.add_format({
    'bold': True,
    'align': 'center',
    'valign': 'vcenter',
    'bg_color': 'yellow',
    'border': 1
})
data_format = workbook.add_format({
    'align': 'center',
    'valign': 'vcenter',
    'bg_color': 'cyan',
    'border': 1,
    'text_wrap': True
})

# Write the headers to the first row
worksheet.write('A1', 'Hostname', header_format)
worksheet.write('B1', 'AD Configuration Status', header_format)
worksheet.write('C1', 'AD Group', header_format)

# Start writing data from the second row
row = 1
for entry in sssd_data:
    worksheet.write(row, 0, entry['hostname'], data_format)
    worksheet.write(row, 1, entry['status'], data_format)
    worksheet.write(row, 2, ', '.join(entry['values']), data_format)
    row += 1

# Set column widths
worksheet.set_column('A:C', 30)

# Close the Excel file
workbook.close()
