import xlsxwriter

# Definisci il percorso del file Excel e del file temporaneo dei dati
report_file = "/root/report/SSSD_Configuration_Report.xlsx"
data_file = "/tmp/sssd_data_temp"

# Leggi i dati dal file temporaneo
with open(data_file, 'r') as file:
    lines = file.readlines()

# Crea un nuovo file Excel e aggiungi un foglio di lavoro
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Definisci le formattazioni come prima

# Intestazioni delle colonne
headers = ['Hostname', 'AD Configuration Status', 'AD Group']
for col, header in enumerate(headers):
    worksheet.write(0, col, header, header_format)

# Scrivi i dati di ogni host nel foglio
for row, line in enumerate(lines, start=1):
    # Dividi ogni riga in base al separatore '|'
    hostname, status, groups = line.strip().split('|')
    worksheet.write(row, 0, hostname, data_format)
    worksheet.write(row, 1, status, data_format)
    worksheet.write(row, 2, groups, data_format)

# Imposta la larghezza delle colonne
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 25)
worksheet.set_column('C:C', 40)

# Chiudi il workbook
workbook.close()
