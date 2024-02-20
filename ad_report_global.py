import xlsxwriter
import sys
import json

# Converti la stringa JSON ricevuta in una struttura dati Python
sssd_data_json = sys.argv[1]
sssd_data = json.loads(sssd_data_json)

# Definisci il percorso del file Excel
report_file = "/root/report/ADGroup_linux_report.xlsx"

# Crea un nuovo file Excel e aggiungi un foglio di lavoro
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Define formatting for headers and data
header_format = workbook.add_format({
    'bold': True,
    'align': 'center',
    'valign': 'vcenter',
    'bg_color': 'yellow',  # Yellow background for the headers
    'border': 1
})
data_format = workbook.add_format({
    'align': 'center',
    'valign': 'vcenter',
    'bg_color': 'cyan',  # Cyan background for the data
    'border': 1,
    'text_wrap': True  # Wrap text in the cell
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
    # Join the AD groups with a newline character to ensure they are listed properly
    worksheet.write(row, 2, "\n".join(entry['values']), data_format)
    row += 1  # Move to the next row for each host

# Set the column widths for clarity
worksheet.set_column('A:C', 30)

# Close the workbook to save the Excel file
workbook.close()
