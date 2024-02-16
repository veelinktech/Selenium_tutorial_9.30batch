import openpyxl

wb = openpyxl.load_workbook('C:\\Users\\pc\\Desktop\\DDF.xlsx')
sheet = wb['Sheet2']

for r in range(1,5):
    for c in range(1,4):
        sheet.cell(row=r, column=c).value='Python'

print('write successfully')
wb.save('C:\\Users\\pc\\Desktop\\DDF.xlsx')