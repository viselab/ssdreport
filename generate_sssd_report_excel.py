import xlsxwriter
import sys
# Ottieni i parametri dalla riga di comando
hostname = sys.argv[1]
sssd_status = sys.argv[2]
sssd_values = sys.argv[3].split(',')  # Presumiamo che i valori siano separati da virgole
sssd_values = sys.argv[3]

# Definisci il percorso del file Excel
report_file = f"/root/report/{hostname}.ADGroup_report.xlsx"
    'align': 'center',
    'valign': 'vcenter',
    'bg_color': 'cyan',  # Sfondo celeste
    'border': 1
    'border': 1,
    'text_wrap': True  # Consente di andare a capo automaticamente nel testo
})

# Scrivi le intestazioni delle colonne con la formattazione delle intestazioni
# Scrivi le intestazioni delle colonne
worksheet.write('A1', 'Hostname', header_format)
worksheet.write('B1', 'AD Configuration Status', header_format)
worksheet.write('C1', 'AD Group', header_format)

# Scrivi il nome dell'host e lo stato della configurazione nelle prime celle
# Scrivi i dati
worksheet.write('A2', hostname, data_format)
worksheet.write('B2', sssd_status, data_format)

# Scrivi ogni gruppo AD in una nuova riga
start_row = 2
for value in sssd_values:
    worksheet.write(start_row, 2, value.strip(), data_format)
    start_row += 1  # Incrementa il numero di riga per ogni gruppo
# Combina tutti i valori di AD Group in una singola stringa separata da newline
ad_groups = "\n".join(sssd_values.split(','))
worksheet.write('C2', ad_groups, data_format)

# Imposta la larghezza delle colonne per migliorare la leggibilità
worksheet.set_column('A:C', 40)  # Aumenta se necessario
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 25)
worksheet.set_column('C:C', 40)

# Chiudi il file Excel
workbook.close()
