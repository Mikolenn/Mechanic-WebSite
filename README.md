# Mechanic-WebSite

Proyecto 2. Laboratorio de Programación y Microcomputadores.

Implementación de la página web para el manejo de citas de un taller mecánico.

Participantes:
Ricardo Arias Castro, B60633.
Luis Guillermo Ramírez, B76222.

Este es el repositorio para el desarrollo del proyecto de la página web, mediante la cual se permite el manejo de citas para un taller mecánico.

La pagina web se compone de dos apps que son Appointments y Register.

Appointments: Se trata de el app principal que se encarga de realizar la creación, eliminación y modificación de citas para el sitio 
web de citas.

Register: Se utiliza para hacer el registro, login y logout de los usuarios.

----------------------------------------------------------------------------------

Para correr el proyecto mediante el Dockerfile, ejecutar los comandos:

$ sudo docker build --tag web:latest .

$ sudo docker run -p 80:80 web:latest

Una vez en aqui, se puede ingresar a la direccion "localhost" directamente en la barra de direcciones




