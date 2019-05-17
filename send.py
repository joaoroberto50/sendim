import xlrd
import pandas as pd
import getpass
import smtplib
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send(d_local, assunto, corpo, user_name, contato, anexo):
	msg = MIMEMultipart()

	msg['From'] = user_name
	msg['To'] = contato
	msg['Subject'] = assunto

	body = corpo

	msg.attach(MIMEText(body, 'plain'))

	anexo = anexo + '.pdf'
	try:
		attachment = open(d_local + anexo, "rb")
	except Exception as error:
		print("ERRO: ", error)
		anexo = anexo[:-4]
		anexo = anexo + '0'
		anexo = anexo + '.pdf'
		try:
			attachment = open(d_local + anexo, "rb")
		except:
			print("No '0' found")
			anexo = anexo[:-5]
			anexo = anexo + ' 0'
			anexo = anexo + '.pdf'
			try:
				attachment = open(d_local + anexo, "rb")
			except Exception as error:
				print("ERRO: ", error)

	try:
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % anexo)
	except Exception as wrong:
		print(wrong)

	try:
		msg.attach(part)
		text = msg.as_string()
		s.sendmail(user_name, contato, text)
		print("E-mail enviado com sucesso para ", contato)
	except Exception as wrong:
		print(wrong)



def runer(nr, p_local, d_local, assunto, corpo, user_name):
	for i in range(0, nr-1):
		contato = planilha['E-mail'][i]
		if(contato!='UERN'):
			anexo = planilha['Matricula'][i]
			send(d_local, assunto, corpo, user_name, contato, anexo)
		else:
			idnt = planilha['Nome'][i]
			print("{} nao possui email".format(idnt))

print("----------- BEM VINDO -----------")
time.sleep(2)
os.system('cls')


logon = False
while(logon == False):
	print("\t\tL O G I N")
	user_name = input("Usuario: ")
	user_pass = getpass.getpass("Senha: ")
	try:
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login(user_name, user_pass)
		logon = True
	except Exception as error:
		os.system('cls')
		print("ERRO: ", error)
		logon = False

datas = False
while(datas == False):
	os.system('cls')
	print("LOGIN efetuado com sucesso")
	print('-'*30)
	assunto = input("insira o assunto do E-mail: ")
	l_txt = input("Insira o local do texto do E-mail com seu formato\nEx.:/home/joao/Downloads/planilha.txt: ")
	p_local = input("Insira o local e o nome da tabela com seu formato\nEx.:/home/joao/Downloads/planilha.xls: ")
	d_local = input("Insira o diretorio onde estao os documentos para anexo\nUsar o char barra invertida no final\nEx.:/home/joao/Downloads/: ")
	print('-'*30)
	tst = False
	while(tst == False):
		qst = input("\nEsta certo desses dados?\n1)Se esta digite 's'\n2)Digite 'm' para modificalos\n\t\t\t  >>> ")
		if(qst == 's'):
			datas = True
			tst = True
		elif(qst == 'm'):
			datas = False
			tst = True
		else:
			os.system('cls')
			print("Entrada invalida - Digite novamente")

texto = open(l_txt, 'r')
corpo = texto.read()

os.system('cls')
print('-' * 30)

try:
	planilha = pd.read_excel(r'' + p_local)
	book = xlrd.open_workbook(p_local)
	sh = book.sheet_by_index(0)
	nr = sh.nrows
except Exception as error:
	print("ERRO: ", error)

runer(nr, p_local, d_local, assunto, corpo, user_name)

print('-' * 30)
x = 0
while(x!=1):
	tst = input("Para sair entre um caracter qualquer: >>> ")
	x = 1

print("----------- Efetuando Logout -----------")
time.sleep(3)
os.system('cls')
print("------------- SAINDO -------------")

s.quit()