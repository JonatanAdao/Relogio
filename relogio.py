# Importando biblioteca Tkinter
import tkinter
from tkinter import *
from tkinter import ttk

# importando biblioteca datetime
from datetime import datetime
#   _______ CORES _________

cor0 = '#ffffff' # branco
cor1 = '#333333' # cinza
cor2 = '#fcc058' # laranja
cor3 = '#fff873' # amarelo
cor4 = '#3297a8' # azul
cor5 = '#fcc058' # laranja
cor6 = '#e85151' # vermelha
cor7 = '#34eb3d' # verde
fundo = '#3b3b3b'

def relogio():  #   função 
    agora = datetime.now()  #   Pega data e hora do sistema  
    dia_semana = agora.strftime('%A')   #   Dia da semana
    dia = agora.day     #   Dia do mês
    mes = agora.strftime('%B')  #   Mês do ano
    ano = agora.strftime('%Y')  #   Ano corrente
    hora = agora.strftime('%H:%M:%S')   #   Horas
    data_d_m_a.config(text= [dia, mes, ano])
    horario.config(text= hora)
    horario.after(200, relogio)     #   Função onde faz os segundos dinamicos
    data_semana.config(text= dia_semana)


'''____Criação e configuração de janela____'''

janela = Tk()
janela.title('RELOGIO')
janela.geometry('310x200')
janela.resizable(width= FALSE, height= FALSE)
janela.configure(bg= fundo)

frame_unico = Frame(janela, width= 310, height= 200, bg= cor1, relief= 'flat')
frame_unico.grid(row= 0,column= 0, sticky= NW)

data =  Label(frame_unico, text='Data :', height= 1, anchor='center', font=('Ivy 20 bold'), bg=cor1, fg= cor0)
data.place(x= 7, y= 20)

data_d_m_a = Label(frame_unico, text= ' ', height= 1, anchor='center', font=('Ivy 20 bold'), bg= cor1, fg= cor4)
data_d_m_a.place(x= 88, y= 20)

data_semana = Label(frame_unico, text= ' ', height= 1, anchor='center', font=('Ivy 20 bold'), bg= cor1, fg= cor4)
data_semana.place(x= 45, y= 50)

horario = Label(frame_unico, text= ' ', height= 2, anchor='center', font=('Ivy 40 bold'), bg= cor1, fg= cor6)
horario.place(x= 5, y= 90)


relogio()
janela.mainloop()
