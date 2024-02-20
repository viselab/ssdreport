import xlsxwriter
import json
import ast

# Dati di esempio passati come argomento dalla riga di comando
sssd_data_string = sys.argv[1]
sssd_data = ast.literal_eval(sssd_data_string)

# Definisci il percorso del file Excel
report_file = "/root/report/ADGroup_linux_report.xlsx"

# Crea un nuovo file Excel e aggiungi un foglio di lavoro
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Imposta la formattazione delle intestazioni e dei dati
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

# Scrivi le intestazioni delle colonne
worksheet.write('A1', 'Hostname', header_format)
worksheet.write('B1', 'AD Configuration Status', header_format)
worksheet.write('C1', 'AD Group', header_format)

# Scrivi i dati di ogni host nel foglio
row = 1
for entry in sssd_data:
    worksheet.write(row, 0, entry['hostname'], data_format)
    worksheet.write(row, 1, entry['status'], data_format)
    worksheet.write(row, 2, entry['values'], data_format)
    row += 1  # Incrementa la riga per ogni host

# Imposta la larghezza delle colonne
worksheet.set_column('A:C', 30)

# Chiudi il file Excel
workbook.close()
