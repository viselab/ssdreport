import json
import sys
import xlsxwriter

# Ottieni i dati come stringa JSON dal primo argomento della riga di comando
data_json = sys.argv[1]

# Converti la stringa JSON in un oggetto Python
try:
    sssd_data = json.loads(data_json)
except json.JSONDecodeError as e:
    print(f"Errore durante il parsing JSON: {e}")
    sys.exit(1)

# Definisci il percorso del file Excel
report_file = "/root/report/ADGroup_linux_report.xlsx"

# Crea un nuovo file Excel e aggiungi un foglio di lavoro
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Definisci la formattazione delle intestazioni e dei dati
header_format = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': 'yellow'})
data_format = workbook.add_format({'align': 'center', 'bg_color': 'cyan', 'text_wrap': True})

# Scrivi le intestazioni delle colonne
worksheet.write('A1', 'Hostname', header_format)
worksheet.write('B1', 'AD Configuration Status', header_format)
worksheet.write('C1', 'AD Group', header_format)

# Scrivi i dati a partire dalla seconda riga
row = 1
for entry in sssd_data:
    worksheet.write(row, 0, entry['hostname'], data_format)
    worksheet.write(row, 1, entry['status'], data_format)
    # Se 'values' è una stringa di gruppi AD separati da virgole, dividi la stringa e uniscila con una virgola e uno spazio
    groups = ', '.join(entry['values'].split(','))
    worksheet.write(row, 2, groups, data_format)
    row += 1

# Imposta la larghezza delle colonne per la leggibilità
worksheet.set_column('A:C', 30)

# Chiudi il workbook per salvare il file Excel
workbook.close()
