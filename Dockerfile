# Definimos OS base
FROM ubuntu:20.04

# Se instala python3 y pip3
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get clean

# Se instalan los requerimientos de la aplicación
RUN pip3 install virtualenv
RUN pip3 install django
RUN pip3 install django-widget-tweaks
RUN pip3 install django-crispy-forms

# El puerto 8000 se expone en el contenedor
EXPOSE 8000

# Se copia la aplicación y sus archivos al directorio /WebSite
ADD . /WebSite
COPY . /WebSite

# Se otorgan permisos sobre el proyecto y el archivo manage.py
RUN chown -R www-data:www-data /WebSite
RUN chmod a+x /WebSite/manage.py

# Se establece el directorio de trabajo
WORKDIR /WebSite

# Se lanza el servidor web del proyecto django
CMD python3 manage.py runserver 0.0.0.0:8000
# CMD python3 manage.py runserver 127.0.0.1:8000