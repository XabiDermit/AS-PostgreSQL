import psycopg2
#import sys

#print(sys.argv[1])

try:

	#conexion con la base de datos
	conexion = psycopg2.connect(database="xabi_as", user="postgres", password="password", host="0.0.0.0", port="5432")

	#creamos un cursor para ejecutar querys
	cursor = conexion.cursor()

	print("Conexión correcta.", "\n")
	print("Informacion sobre la conexión: ")
	print(conexion.get_dsn_parameters(), "\n")

	#creamos una tabla, añadimos valores y hacemos una consulta select
	cursor.execute("DROP TABLE IF EXISTS pruebas_as;")
	cursor.execute("CREATE TABLE pruebas_as (id varchar(50) PRIMARY KEY, nombre varchar(50) UNIQUE NOT NULL);")
	cursor.execute("INSERT INTO pruebas_as (id,nombre) VALUES ('1234', 'xabi');")
	cursor.execute("SELECT * from pruebas_as;")

	#comprobamos que ha funcionado
	record = cursor.fetchall()
	print ("Info:" , record)

	#cerramos la conexion
	cursor.close()
	conexion.close()
	print("Conexion cerrada")

#excepcion si sale mal la conexión
except (Exception, psycopg2.Error) as error:
	print("Error en la conexion: ", error)


		

