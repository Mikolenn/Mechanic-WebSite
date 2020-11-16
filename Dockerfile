# Base image
FROM python:3


# Basic information
LABEL maintainers = "ricardo.arias@ucr.ac.cr,luisguillermo.ramirez@ucr.ac.cr"
LABEL version="1.0"
LABEL description = "Proyecto Django"


# Define working directory
WORKDIR /WebSite

# Install django
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
ADD . /WebSite
COPY . /WebSite
# Expose port 80
EXPOSE 8000

# Run application
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
