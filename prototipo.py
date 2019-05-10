planilha = [['Nadja', 'nadja@email.com'], ['Carmen', 'carmen@email.com'], ['Marcio', 'marcio@email.com'], ['Amanda', 'amanda@email.com'], ['Joao', 'joao@email.com']]

diretorio = ['Nadja', 'Carmen', 'Marcio', 'Amanda', 'Joao']

assunto = input("Assunto do email: ")

corpo = input("Corpo do email: ")

tamanho_planilha = 0

for i in planilha:
	tamanho_planilha+=1

tamanho_diretorio = 0

for i in diretorio:
	tamanho_diretorio+=1

anexo = ''
email = ''

for i in range(0, tamanho_planilha):
	for j in range(0, tamanho_diretorio):
		if(diretorio[j]==planilha[i][0]):
			anexo = diretorio[j]
	email = planilha[i][1]
	print("Aassunto: ", assunto)
	print("Email:\n ", corpo)
	print("Destino: ", email)
	print("Anexo: ", anexo, ".pdf")
