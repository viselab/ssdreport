import sys
import xlsxwriter

# Leggi i dati come una singola stringa dal primo argomento della riga di comando
sssd_data_string = sys.argv[1]

# Dividi la stringa in righe separate, ogni riga rappresenta i dati di un host
sssd_data_lines = sssd_data_string.strip().split('\n')

# Definisci il percorso del file Excel
report_file = "/root/report/ADGroup_linux_report.xlsx"

# Crea un nuovo file Excel e aggiungi un foglio di lavoro
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Definisci la formattazione delle intestazioni e dei dati
header_format = workbook.add_format({
    'bold': True,
    'align': 'center',
    'bg_color': 'yellow'
})
data_format = workbook.add_format({
    'align': 'center',
    'bg_color': 'cyan',
    'text_wrap': True
})

# Scrivi le intestazioni delle colonne
worksheet.write('A1', 'Hostname', header_format)
worksheet.write('B1', 'AD Configuration Status', header_format)
worksheet.write('C1', 'AD Group', header_format)

# Scrivi i dati a partire dalla seconda riga
row = 1
for line in sssd_data_lines:
    if line:  # Assicurati che la riga non sia vuota
        hostname, status, values = line.split(':')
        worksheet.write(row, 0, hostname, data_format)
        worksheet.write(row, 1, status, data_format)
        # Assicurati che i gruppi AD siano separati da una virgola e uno spazio
        groups = values.replace(',', ', ')
        worksheet.write(row, 2, groups, data_format)
        row += 1

# Imposta la larghezza delle colonne per la leggibilità
worksheet.set_column('A:C', 30)

# Chiudi il workbook per salvare il file Excel
workbook.close()
