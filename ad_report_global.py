import json
import sys
import xlsxwriter

# Controlla se è stato fornito un argomento da riga di comando
if len(sys.argv) < 2:
    print("Usage: python generate_sssd_report_excel.py '<json_data>'")
    sys.exit(1)

# Carica i dati SSSD passati come stringa JSON dal primo argomento della riga di comando
sssd_data_json = sys.argv[1]
try:
    sssd_data = json.loads(sssd_data_json)
except json.JSONDecodeError as e:
    print("Error decoding JSON: ", e)
    sys.exit(1)

# Definisci il percorso del file Excel
report_file = "/root/report/ADGroup_linux_report.xlsx"

# Crea un nuovo file Excel e aggiungi un foglio di lavoro
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Imposta la formattazione delle intestazioni
header_format = workbook.add_format({
    'bold': True,
    'align': 'center',
    'valign': 'vcenter',
    'bg_color': 'yellow',  # Sfondo giallo per le intestazioni
    'border': 1
})

# Imposta la formattazione dei dati
data_format = workbook.add_format({
    'align': 'center',
    'valign': 'vcenter',
    'bg_color': 'cyan',  # Sfondo celeste per i dati
    'border': 1,
    'text_wrap': True  # Attiva il testo a capo automatico
})

# Scrivi le intestazioni delle colonne
worksheet.write('A1', 'Hostname', header_format)
worksheet.write('B1', 'AD Configuration Status', header_format)
worksheet.write('C1', 'AD Group', header_format)

# Scrivi i dati di ogni host nel foglio
row = 1
for host_data in sssd_data:
    worksheet.write(row, 0, host_data['hostname'], data_format)
    worksheet.write(row, 1, host_data['status'], data_format)
    worksheet.write(row, 2, host_data['values'], data_format)
    row += 1  # Incrementa la riga per ogni host

# Imposta la larghezza delle colonne
worksheet.set_column('A:C', 30)

# Chiudi il workbook per salvare il file Excel
workbook.close()
