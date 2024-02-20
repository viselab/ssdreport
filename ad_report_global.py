import xlsxwriter
import json
import sys

# Carica i dati JSON passati dal playbook
data = json.loads(sys.argv[1])

# Definisci il percorso del file Excel
report_file = "/root/report/SSSD_Configuration_Report.xlsx"

# Crea un nuovo file Excel e aggiungi un foglio di lavoro
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Formattazioni
header_format = workbook.add_format({
    'bold': True,
    'align': 'center',
    'valign': 'vcenter',
    'bg_color': '#000000',  # RGB per ciano
    'font_color': '#00FFFF'  # RGB per nero
})
data_format = workbook.add_format({
    'align': 'center',
    'valign': 'vcenter',
    'bg_color': '#FFFF00',  # RGB per giallo
    'font_color': '#000000',  # RGB per nero
    'text_wrap': True
})

# Intestazioni delle colonne
headers = ['Hostname', 'AD Configuration Status', 'AD Group']
for col, header in enumerate(headers):
    worksheet.write(0, col, header, header_format)

# Scrivi i dati di ogni host nel foglio
for row, line in enumerate(data, start=1):
    # Dividi ogni riga in base al separatore '|'
    hostname, status, groups = line.split('|')
    worksheet.write(row, 0, hostname, data_format)
    worksheet.write(row, 1, status, data_format)
    # Unisci tutti i gruppi in una singola stringa separata da virgole
    groups_combined = ', '.join(groups.split(','))  # Unisce i gruppi e aggiunge una virgola tra di loro
    worksheet.write(row, 2, groups_combined, data_format)

# Imposta la larghezza delle colonne
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 25)
worksheet.set_column('C:C', 40)

# Chiudi il workbook
workbook.close()
