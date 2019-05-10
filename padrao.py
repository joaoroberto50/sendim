import xlrd

book = xlrd.open_workbook("/home/joao/Documentos/Sem1.xls")
print ("Número de abas: ", book.nsheets)
print ("Nomes das Planilhas:", book.sheet_names())
sh = book.sheet_by_index(0)
x = sh.nrows
print(x)
'''print("Valor da célula D30 é ", sh.cell_value(rowx=29, colx=3))
for rx in range(sh.nrows):
    print(sh.row(rx))'''
