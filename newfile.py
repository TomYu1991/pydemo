import openpyxl
file=open(r"C:\Users\user\Desktop\myname.txt",'r')
wb=openpyxl.Workbook()
sheet=wb.get_active_sheet()
count=1
for line in file.readlines():
    sheet.cell(count,1).value=line
    count+=1
wb.save(r"C:\Users\user\Desktop\m.xlsx")
wb.close()
print('over!')
