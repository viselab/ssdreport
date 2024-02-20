import sys
import xlsxwriter

# Prendi i parametri dalla riga di comando
hostname = sys.argv[1]
sssd_status = sys.argv[2]
sssd_values = sys.argv[3]

# Definisci il percorso del file Excel
report_file = f"/root/report/{hostname}_sssd_report.xlsx"

# Crea un nuovo file Excel e aggiungi un foglio di lavoro
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Imposta le intestazioni delle colonne
worksheet.write('A1', 'Hostname')
worksheet.write('B1', 'SSSD Configuration Status')
worksheet.write('C1', 'SSSD Configuration Values')

# Aggiungi i dati nelle celle
worksheet.write('A2', hostname)
worksheet.write('B2', sssd_status)
worksheet.write('C2', sssd_values)

# Chiudi il file Excel
workbook.close()
