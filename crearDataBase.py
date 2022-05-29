import mysql.connector # importacion de conector MySQL

#Conexion con Servidor
serverdb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

#Mensaje de conexion de base de datos, si el objeto se crea esta bien la conexion
print(serverdb)

mycursor = serverdb.cursor()

mycursor.execute("CREATE DATABASE estacionamiento")

mycursor.execute("SHOW DATABASES")

#Lista de bases de datos creadas
for x in mycursor:
    print(x)