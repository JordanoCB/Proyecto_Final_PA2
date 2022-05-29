import mysql.connector # importacion de conector MySQL

#Conexion con Servidor

serverdb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='estacionamiento'
)

print(serverdb)

mycursor = serverdb.cursor()

#Crear base de dato estaciona
mycursor.execute("CREATE TABLE estaciona (ticket INT(10) PRIMARY KEY,patente VARCHAR(8), fechaEntrada Datetime, fechaSalida Datetime, total int(10), cerrado int(1))")

#chekeo de creacion, visualizando las tablas creadas en la base de datos "Estacionamiento"
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)