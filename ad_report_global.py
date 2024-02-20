import xlsxwriter
import json
import sys

# Assicurati che almeno un argomento sia stato passato (la stringa JSON con i dati)
if len(sys.argv) < 2:
    print("Errore: Nessun dato fornito allo script.")
    sys.exit(1)

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
    'bg_color': 'yellow',
    'border': 1
})
data_format = workbook.add_format({
    'align': 'center',
    'valign': 'vcenter',
    'border': 1,
    'text_wrap': True
})

# Intestazioni delle colonne
headers = ['Hostname', 'AD Configuration Status', 'AD Group']
for col, header in enumerate(headers):
    worksheet.write(0, col, header, header_format)

# Scrivi i dati di ogni host nel foglio
for row, line in enumerate(data, start=1):
    # Dividi ogni riga in base al separatore '|'
    # Assicurati che la stringa di dati sia strutturata come previsto
    try:
        hostname, status, groups = line.split('|')
    except ValueError:
        print(f"Errore nella decodifica della riga: {line}")
        continue  # Salta questa riga se ci sono problemi nella divisione

    worksheet.write(row, 0, hostname, data_format)
    worksheet.write(row, 1, status, data_format)
    worksheet.write(row, 2, groups, data_format)

# Imposta la larghezza delle colonne
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 25)
worksheet.set_column('C:C', 40)

# Chiudi il workbook
workbook.close()
