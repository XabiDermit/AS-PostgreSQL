import psycopg2 as postgres

conexion = postgres.connect(database="postgres", user='postgres', password='xabi_as_postgres', host="localhost", port=5432)

cursor = connection.cursor()

sentencia_sql ="CREATE TABLE pruebas_as (id varchar(50) PRIMARY KEY, nombre varchar(50) UNIQUE NOT NULL);"

cursor.execute(sentencia_sql)

#para hacer pruebas

record = cursor.fetchall()
print ("Info:" , record)

