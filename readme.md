Trabajo de Administracion de sistemas sobre la imagen PostgreSQL de DockerHub

Pequeña explicación de cada archivo:

  - docker-compose.yml --> Archivo de configuracion del entorno Docker Compose
  - Carpeta appcliente:
      - appcliente.py --> Aplicación cliente
      - Dockerfile --> Archivo de configuración de la imagen creada para encapsular la aplicación cliente
  - Carpeta vagrant:
      - Vagrantfile --> Archivo de configuración de la maquina virtual creada con Vagrant
      - Carpeta .vagrant: archivos creados al ejecutar el Vagrantfile 
      - Carpeta archivos: 
          - appcliente.py --> Aplicación cliente modificada para la nueva conexión en la maquina virtual
          - dependencias.sh --> Archivo bash que instala las dependencias requeridas por la app cliente
          - crearUsuario.sh --> Archivo bash que crea un nuevo usuario en la base de datos de Postgres al que conectarse
