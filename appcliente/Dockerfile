#Usamos la imagen oficial de python (la ultima version) como base para nuestra imagen
FROM python:3.6.12

#Seleccionamos el directorio /usr/scr/app como nuestro directorio de trabajo
WORKDIR /usr/scr/app

#instalamos las dependencias que necesite nuestre programa
RUN pip install psycopg2
#Copiamos al directorio de trabajo el fichero .py que vamos a ejecutar 
COPY appcliente.py ./

#Definimos el comando de arranque
CMD ["python", "./appcliente.py"]





