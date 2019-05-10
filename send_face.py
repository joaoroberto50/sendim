from tkinter import *

def Next(assunto, corpo):
	print(assunto)
	print(corpo)


j = Tk()

j.geometry("500x500")

j.title("Login:")

texto = Label(j, text = "\nAssunto")
texto.pack()

assunto = Entry(j)
assunto.pack()

texto = Label(j, text = "\nCorpo")
texto.pack()

corpo = Entry(j)
corpo.pack()

b = Button(j, text = "Next >>", bg = 'red', fg = 'yellow', comand = Next(assunto, corpo))
b.pack()

j.mainloop()
