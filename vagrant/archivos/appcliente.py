import psycopg2

try:

	#conexion con la base de datos
	conexion = psycopg2.connect(database="postgres", user="xabiadmin", password="xabi1234", host="localhost", port="5432")

	#creamos un cursor para ejecutar querys
	cursor = conexion.cursor()

	print("########################################  Conexión correcta  ###################################", "\n")
	print("Informacion sobre la conexión: ")
	print(conexion.get_dsn_parameters(), "\n")

	#creamos una tabla, añadimos valores y hacemos una consulta select
	cursor.execute("DROP TABLE IF EXISTS pruebas_as;")
	print("Creando la tabla pruebas_as, que almacena un id y un nombre.....")
	print("########################################  Tabla creada  ####################################### ","\n")
	cursor.execute("CREATE TABLE pruebas_as (id varchar(50) PRIMARY KEY, nombre varchar(50) UNIQUE NOT NULL);")
	print("Insertando el id '1234' y el nombre 'xabi' en la tabla pruebas_as.....")
	print("########################################  Datos insertados en la tabla  #######################", "\n")
	cursor.execute("INSERT INTO pruebas_as (id,nombre) VALUES ('1234', 'xabi');")
	print("Seleccionando los datos que guarda la tabla pruebas_as.....")
	cursor.execute("SELECT * from pruebas_as;")

	#comprobamos que ha funcionado
	record = cursor.fetchall()
	print ("Datos que guarda la tabla pruebas_as:" , record, "\n")

	#cerramos la conexion
	cursor.close()
	conexion.close()
	print("#######################################  Conexion cerrada  ######################################")

#excepcion si sale mal la conexión
except (Exception, psycopg2.Error) as error:
	print("Error en la conexion: ", error)


		
