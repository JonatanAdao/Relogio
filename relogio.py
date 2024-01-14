# Importando biblioteca Tkinter
import tkinter
from tkinter import *
from tkinter import ttk

# importando biblioteca datetime
from datetime import datetime


agora = datetime.now()
dia = agora.day
mes = agora.month
ano = agora.year
div = '/'
hora = agora.hour
minutos = agora.minute
segundos = agora.second
div_1 = ':'

#_______ CORES _________

cor0 = '#ffffff' # branco
cor1 = '#333333' # cinza
cor2 = '#fcc058' # laranja
cor3 = '#fff873' # amarelo
cor4 = '#3297a8' # azul
cor5 = '#fcc058' # laranja
cor6 = '#e85151' # vermelha
cor7 = '#34eb3d' # verde
fundo = '#3b3b3b'

'''____Criação e configuração de janela____'''


janela = Tk()
janela.title('RELOGIO')
janela.geometry('280x200')
janela.configure(bg= fundo)

frame_unico = Frame(janela, width= 280, height= 200, bg= cor1, relief= 'flat')
frame_unico.grid(row= 0,column= 0, sticky= NW)

data =  Label(frame_unico, text='Data :', height= 1, anchor='center', font=('Ivy 20 bold'), bg=cor1, fg= cor0)
data.place(x= 20, y= 20)

data_d_m_a = Label(frame_unico, text= [dia, div, mes, div, ano], height= 1, anchor='center', font=('Ivy 20 bold'), bg= cor1, fg= cor4)
data_d_m_a.place(x= 100, y= 20)


horario = Label(frame_unico, text= [hora, div_1, minutos,div_1, segundos], height= 2, anchor='center', font=('Ivy 40 bold'), bg= cor1, fg= cor6)
horario.place(x= 5, y= 50)

print(agora)
print(dia,mes,ano)


janela.mainloop()
