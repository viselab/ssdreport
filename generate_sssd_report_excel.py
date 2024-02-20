import sys
import xlsxwriter

# Prendi i parametri dalla riga di comando
hostname = sys.argv[1]
sssd_status = sys.argv[2]
sssd_values = sys.argv[3].split(',')  # Supponendo che i valori siano separati da virgole

# Definisci il percorso del file Excel
report_file = f"/root/report/{hostname}.ADGroup_report.xlsx"

# Crea un nuovo file Excel e aggiungi un foglio di lavoro
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Imposta la formattazione delle intestazioni
header_format = workbook.add_format({
    'bold': True,
    'align': 'center',       # Centra il testo
    'valign': 'vcenter',     # Centra verticalmente
    'bg_color': '#FFFF00',   # Sfondo giallo
    'border': 1              # Aggiunge un bordo
})

# Scrivi le intestazioni delle colonne con la formattazione
worksheet.write('A1', 'Hostname', header_format)
worksheet.write('B1', 'AD Configuration Status', header_format)
worksheet.write('C1', 'AD Group', header_format)

# Scrivi il nome dell'host e lo stato della configurazione nelle prime celle con formattazione centrata
worksheet.write('A2', hostname, header_format)
worksheet.write('B2', sssd_status, header_format)

# Scrivi ogni gruppo AD in una nuova riga
start_row = 2
for group in sssd_values:
    worksheet.write('C' + str(start_row), group.strip(), header_format)
    start_row += 1

# Imposta la larghezza delle colonne per migliorare la leggibilità
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 25)
worksheet.set_column('C:C', 40)

# Chiudi il file Excel
workbook.close()
