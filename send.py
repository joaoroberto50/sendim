import xlrd
import pandas as pd
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from unidecode import unidecode

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

	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % anexo)

	msg.attach(part)
	text = msg.as_string()
	s.sendmail(user_name, contato, text)
	print("E-mail enviado com sucesso para ", contato)



def runer(nr, p_local, d_local, assunto, corpo, user_name):
	for i in range(0, nr-1):
		contato = planilha['E-mail'][i]
		anexo = planilha['Nome'][i]
		anexo = (unidecode(anexo))
		send(d_local, assunto, corpo, user_name, contato, anexo)



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
		print("ERRO: ", error)
		logon = False

assunto = input("insira o assunto do E-mail: ")
l_txt = input("Insira o local do texto do E-mail com seu formato\nEx.:/home/joao/Downloads/planilha.txt: ")
texto = open(l_txt, 'r')
corpo = texto.read()
#texto.close()
p_local = input("Insira o local e o nome da tabela com seu formato\nEx.:/home/joao/Downloads/planilha.xml: ")
d_local = input("Insira o diretorio onde estao os documentos para anexo\nEx.:/home/joao/Downloads/: ")
d_local = d_local + '/'

try:
	planilha = pd.read_excel(r'' + p_local)
	book = xlrd.open_workbook(p_local)
	sh = book.sheet_by_index(0)
	nr = sh.nrows
except Exception as error:
	print("ERRO: ", error)

runer(nr, p_local, d_local, assunto, corpo, user_name)

s.quit()