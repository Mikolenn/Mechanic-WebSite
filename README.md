# Mechanic-WebSite

Proyecto 2. Laboratorio de Programación y Microcomputadores.

Implementación de la página web para el manejo de citas de un taller mecánico.

Participantes:
Ricardo Arias Castro, B60633.
Luis Guillermo Ramírez, B76222.

Este es el repositorio para el desarrollo del proyecto de la página web, mediante la cual se permite el manejo de citas para un taller mecánico.

Para correr el proyecto mediante el Dockerfile, ejecutar los comandos:

$ sudo docker build --tag website:latest .
$ sudo docker run -ti website:latest bash

Una vez en el bash, ejecute el comando:

$ python3 manage.py runserver 0.0.0.0:8000
