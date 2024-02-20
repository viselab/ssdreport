import sys
import xlsxwriter

hostname = sys.argv[1]
status = sys.argv[2]
value = sys.argv[3]
file_path = "/path/to/report/directory/" + hostname + "_sssd_report.xlsx"

workbook = xlsxwriter.Workbook(file_path)
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hostname')
worksheet.write('B1', 'SSSD Configuration Status')
worksheet.write('C1', 'SSSD Configuration Value')

worksheet.write('A2', hostname)
worksheet.write('B2', status)
worksheet.write('C2', value)

workbook.close()
