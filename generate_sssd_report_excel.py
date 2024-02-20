import xlsxwriter
import sys

# Ottieni i parametri dalla riga di comando
hostname = sys.argv[1]
sssd_status = sys.argv[2]
sssd_values = sys.argv[3]

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
    'border': 1,
    'text_wrap': True  # Consente di andare a capo automaticamente nel testo
})

# Scrivi le intestazioni delle colonne
worksheet.write('A1', 'Hostname', header_format)
worksheet.write('B1', 'AD Configuration Status', header_format)
worksheet.write('C1', 'AD Group', header_format)

# Scrivi i dati
worksheet.write('A2', hostname, data_format)
worksheet.write('B2', sssd_status, data_format)

# Combina tutti i valori di AD Group in una singola stringa separata da newline
ad_groups = "\n".join(sssd_values.split(','))
worksheet.write('C2', ad_groups, data_format)

# Imposta la larghezza delle colonne per migliorare la leggibilità
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 25)
worksheet.set_column('C:C', 40)

# Chiudi il file Excel
workbook.close()
