import sys
import xlsxwriter

# Ipotizziamo di ricevere i dati da qualche parte del tuo script o del tuo playbook Ansible
hostname = 'rhel7to8-02'
sssd_status = 'Config OK'
sssd_values = ['GSS_Unix_Administrators', 'GRA_PREP_ADOPT_Admins@adgr.net', 'GRAP_ADOPT_PREP_EXT@adgr.net']

# Definisci il percorso del file Excel
report_file = f"/root/report/{hostname}_ADGroup_report.xlsx"

# Crea un nuovo file Excel e aggiungi un foglio di lavoro
workbook = xlsxwriter.Workbook(report_file)
worksheet = workbook.add_worksheet()

# Imposta la formattazione delle intestazioni
header_format = workbook.add_format({
    'bold': True,
    'align': 'center',
    'valign': 'vcenter',
    'bg_color': '#FFFF00',  # Giallo
    'border': 1
})

# Imposta la formattazione dei dati
data_format = workbook.add_format({
    'align': 'center',
    'valign': 'vcenter',
    'bg_color': '#00B0F0',  # Celeste
    'border': 1
})

# Scrivi le intestazioni delle colonne con la formattazione delle intestazioni
worksheet.write('A1', 'Hostname', header_format)
worksheet.write('B1', 'AD Configuration Status', header_format)
worksheet.write('C1', 'AD Group', header_format)

# Scrivi i dati con la formattazione dei dati
worksheet.write('A2', hostname, data_format)
worksheet.write('B2', sssd_status, data_format)

# Scrivi ogni gruppo AD in una nuova riga
for row_num, group in enumerate(sssd_values, start=2):
    worksheet.write(row_num, 2, group, data_format)

# Imposta la larghezza delle colonne per migliorare la leggibilità
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 25)
worksheet.set_column('C:C', 40)

# Chiudi il file Excel
workbook.close()

# Chiudi il file Excel
workbook.close()
