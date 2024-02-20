import json
import sys
import xlsxwriter

# Load the SSSD data from the JSON input
sssd_data = json.loads(sys.argv[1])

# Excel file path
report_file = "/root/report/ADGroup_linux_report.xlsx"

# Create an Excel workbook and worksheet
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Define the formatting
header_format = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': 'yellow'})
data_format = workbook.add_format({'align': 'center', 'bg_color': 'cyan', 'text_wrap': True})

# Write headers
worksheet.write('A1', 'Hostname', header_format)
worksheet.write('B1', 'AD Configuration Status', header_format)
worksheet.write('C1', 'AD Group', header_format)

# Write data
row = 1
for entry in sssd_data:
    worksheet.write(row, 0, entry['hostname'], data_format)
    worksheet.write(row, 1, entry['status'], data_format)
    worksheet.write(row, 2, ", ".join(entry['values']), data_format)
    row += 1

# Close the workbook
workbook.close()
