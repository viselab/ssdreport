import sys
import xlsxwriter

# Prendi i parametri dalla riga di comando
hostname = sys.argv[1]
sssd_status = sys.argv[2]
sssd_values = sys.argv[3].split(',')  # Supponendo che i valori siano separati da virgole

# Definisci il percorso del file Excel
report_file = f"/root/report/{hostname}_sssd_report.xlsx"

# Crea un nuovo file Excel e aggiungi un foglio di lavoro
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Imposta le intestazioni delle colonne e la formattazione
header_format = workbook.add_format({'bold': True, 'font_color': 'blue'})
worksheet.write('A1', 'Hostname', header_format)
worksheet.write('B1', 'SSSD Configuration Status', header_format)
worksheet.write('C1', 'SSSD Configuration Values', header_format)

# Aggiungi i dati nelle celle con formattazione
data_format = workbook.add_format({'text_wrap': True})
worksheet.write('A2', hostname)
worksheet.write('B2', sssd_status)
row = 2
for value in sssd_values:
    worksheet.write(row, 2, value, data_format)
    row += 1

# Imposta la larghezza delle colonne per migliorare la leggibilità
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 25)
worksheet.set_column('C:C', 40)

# Chiudi il file Excel
workbook.close()
