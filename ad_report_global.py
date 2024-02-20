import json
import sys
import xlsxwriter

# Attempt to parse the JSON data passed from the Ansible playbook
try:
    sssd_data = json.loads(sys.argv[1])
except json.JSONDecodeError as e:
    print(f"Failed to parse JSON data: {e}")
    sys.exit(1)

# Define the path for the Excel report
report_file = "/root/report/ADGroup_linux_report.xlsx"

# Create the Excel workbook and worksheet
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Define formats for the header and data cells
header_format = workbook.add_format({'bold': True, 'bg_color': 'yellow', 'align': 'center'})
data_format = workbook.add_format({'bg_color': 'cyan', 'align': 'center', 'valign': 'top', 'text_wrap': True})

# Write the header row
worksheet.write('A1', 'Hostname', header_format)
worksheet.write('B1', 'AD Configuration Status', header_format)
worksheet.write('C1', 'AD Group', header_format)

# Start at the first data row
row = 1
for item in sssd_data:
    worksheet.write(row, 0, item['hostname'], data_format)
    worksheet.write(row, 1, item['status'], data_format)
    worksheet.write(row, 2, item['values'], data_format)
    row += 1

# Close the workbook to finalize the Excel file
workbook.close()
