from tkinter import *
from tkinter import messagebox
import datetime
import mysql.connector

precio=4
def insertar():
    label_mostrar["text"]=""
    serverdb = mysql.connector.connect(host='localhost',user='root',password='',database='estacionamiento')
    insertar = serverdb.cursor()
    sql= "INSERT INTO estaciona (ticket, patente, fechaEntrada,fechaSalida,total,cerrado) VALUES (%s, %s, %s, %s, %s, %s)"
    s = serverdb.cursor()
    s.execute("SELECT * FROM estaciona")
    #Campos digitados por pantalla de los campos solicitados por la tabla
    ticket = len(s.fetchall())+1
    patente = cajatxt1_e1.get()
    fechaEntrada = datetime.datetime.now()
    fechaSalida = ""
    total = ""
    val= (ticket,patente,fechaEntrada,fechaSalida,total,0)
    #Ejecucion de la insercion de campos
    insertar.execute(sql, val)
    serverdb.commit()
    formato="Ticket: {}".format(ticket), "\nPatente: {}".format(patente), "\nFecha Entrada: {}".format(fechaEntrada)
    label_mostrar["text"]=formato

def calcular():
    label_mostrar["text"]=""
    #Conexion con Servidor
    serverdb = mysql.connector.connect(host='localhost',user='root',password='',database='estacionamiento')
    s=serverdb.cursor()
    ticket = cajatxt1_e2.get()
    s.execute("SELECT patente FROM estaciona Where ticket="+ticket)
    for x in s:
        patente=x[0]
    s.execute("SELECT fechaEntrada FROM estaciona Where ticket="+ticket)
    for x in s:
        fechaEntrada=x[0]
    fechaSalida = datetime.datetime.now()
    diferencia=fechaSalida-fechaEntrada
    total = (diferencia.total_seconds()/60)*precio
    s.execute("SELECT cerrado FROM estaciona Where ticket="+ticket)
    for x in s:
        cerrado=x[0]
    if cerrado == 0:
        serverdb = mysql.connector.connect(host='localhost',user='root',password='',database='estacionamiento')
        mycursor = serverdb.cursor()
        sql = "UPDATE estaciona SET fechaSalida = %s, total = %s,cerrado = 1 WHERE ticket = %s"
        mycursor.execute(sql,(fechaSalida,total,ticket))
        serverdb.commit()
        mycursor.close()
        formatoif="Total: ${:,.0f}".format(total),"\nTicket: {}".format(ticket),"\nPatente: {}".format(patente),"\nFecha Entrada: {}".format(fechaEntrada),"\nFecha Salida: {}".format(datetime.datetime.strftime(fechaSalida, '%d-%m-%Y %H:%M'))
        label_mostrar["text"]=formatoif
    else:
        formatoelse="Documento Cerrado previamente"
        label_mostrar["text"]=formatoelse

ventana = Tk()
ventana.title('Estacionamiento')
ventana.geometry('650x650')

#Caja1

e1=LabelFrame(ventana,width=100,text="Ingreso",highlightbackground='red',highlightthickness=1)
e1.grid(row=0,column=0,padx=10,pady=10,ipadx=10,ipady=10)

l1_e1=Label(e1,text="Patente",fg="blue",font=8)
l1_e1.grid(row=0,column=0,padx=5,pady=5,ipadx=5,ipady=5)
cajatxt1_e1=Entry(e1,fg="blue",font=8,width=15)
cajatxt1_e1.grid(row=0,column=1)

boton1_e1=Button(e1,text="Ingresar",fg="blue",font=8,command=insertar)
boton1_e1.grid(row=1,column=1,sticky=W)

#Caja2

e2=LabelFrame(ventana,width=100,text="Salida",highlightbackground='red',highlightthickness=1)
e2.grid(row=0,column=1,padx=10,pady=10,ipadx=10,ipady=10)

l1_e2=Label(e2,text="N° Ticket",fg="blue",font=8)
l1_e2.grid(row=0,column=0,padx=5,pady=5,ipadx=5,ipady=5)
cajatxt1_e2=Entry(e2,fg="blue",font=8,width=15)
cajatxt1_e2.grid(row=0,column=1)

boton1_e2=Button(e2,text="Finalizar servicio",fg="blue",font=8,command=calcular)
boton1_e2.grid(row=5,column=1,sticky=W)

#cajaFinal

mostrar=LabelFrame(ventana,width=100,text="Mostrar Ticket",highlightbackground='red',highlightthickness=1)
mostrar.grid(row=1,column=0,padx=10,pady=10,ipadx=10,ipady=10)

label_mostrar=Label(mostrar,text="",fg="blue",font=8)
label_mostrar.grid(row=0,column=0,padx=5,pady=5,ipadx=5,ipady=5)
#cajatxt1_mostrar=Entry(mostrar,fg="blue",font=8,width=10)
#cajatxt1_mostrar.grid(row=0,column=1)

ventana.mainloop()