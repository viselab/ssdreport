import xlsxwriter
import sys

# Ottieni i parametri dalla riga di comando
hostname = sys.argv[1]
sssd_status = sys.argv[2]
sssd_values = sys.argv[3].split(',')  # Presumiamo che i valori siano separati da virgole

# Definisci il percorso del file Excel
report_file = f"/root/report/{hostname}.ADGroup_report.xlsx"

# Crea un nuovo file Excel e aggiungi un foglio di lavoro
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Imposta la formattazione delle intestazioni
header_format = workbook.add_format({
    'bold': True,
    'align': 'center',
    'valign': 'vcenter',
    'bg_color': 'yellow',  # Sfondo giallo
    'border': 1
})

# Imposta la formattazione dei dati
data_format = workbook.add_format({
    'align': 'center',
    'valign': 'vcenter',
    'bg_color': 'cyan',  # Sfondo celeste
    'border': 1
})

# Scrivi le intestazioni delle colonne con la formattazione delle intestazioni
worksheet.write('A1', 'Hostname', header_format)
worksheet.write('B1', 'AD Configuration Status', header_format)
worksheet.write('C1', 'AD Group', header_format)

# Scrivi il nome dell'host e lo stato della configurazione nelle prime celle
worksheet.write('A2', hostname, data_format)
worksheet.write('B2', sssd_status, data_format)

# Scrivi ogni gruppo AD in una nuova riga
start_row = 2
for value in sssd_values:
    worksheet.write(start_row, 2, value.strip(), data_format)
    start_row += 1  # Incrementa il numero di riga per ogni gruppo

# Imposta la larghezza delle colonne per migliorare la leggibilità
worksheet.set_column('A:C', 30)  # Aumenta se necessario

# Chiudi il file Excel
workbook.close()
