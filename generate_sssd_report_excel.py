import sys
import xlsxwriter

# Ottieni i valori dalla riga di comando
hostname = sys.argv[1]
sssd_status = sys.argv[2]
sssd_value = sys.argv[3]
output_file = f"{hostname}_sssd_report.xlsx"

# Crea un nuovo workbook e un worksheet
workbook = xlsxwriter.Workbook(output_file)
worksheet = workbook.add_worksheet()

# Imposta le intestazioni
worksheet.write('A1', 'Hostname')
worksheet.write('B1', 'SSSD Configuration Status')
worksheet.write('C1', 'SSSD Configuration Value')

# Aggiungi i dati
worksheet.write('A2', hostname)
worksheet.write('B2', sssd_status)
worksheet.write('C2', sssd_value)

# Chiudi il workbook
workbook.close()
