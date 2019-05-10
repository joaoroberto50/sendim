import pandas as pd
import ezodf

x = pd.read_excel(r'/home/joao/Documentos/Sem1.xls')
for df in x:
	print(df)
print(x)
