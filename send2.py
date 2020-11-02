import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


fromaddr = "origem@email.com"
toaddr = "destino@email.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test 2 com anexo"

body = "Esse é o teste 2 de um email com anexo.\nFavor nao responder."

msg.attach(MIMEText(body, 'plain'))

filename = "Bojack.png"
attachment = open("/home/joao/Downloads/Bojack.png", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "******")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()
