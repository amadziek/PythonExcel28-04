import openpyxl

wb = openpyxl.load_workbook('./data/videogamesales.xlsx')
ws = wb.active
print(ws)

ws = wb['vgsales']

print("total number of ros: " + str(ws.max_row))  # total number of ros: 16328
print("total number of columns" + str(ws.max_column))  # total number of columns10

print("Vaule in cell A1 is: " , ws['A1'].value) # Vaule in cell A1 is:  Rank

values = [ws.cell(row=1, column=i).value for i in range(1, ws.max_column)]
print(values)  # ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales']

