import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("joaoroberto.jr35@gmail.com", "******")

msg = "Test 01!"
s.sendmail("joaoroberto.jr35@gmail.com", "joaorobertomendez@hotmail.com", msg)
s.quit()