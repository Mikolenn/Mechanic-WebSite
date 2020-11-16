from django.db import models
from django.contrib.auth.models import User


# Opciones para la selección de la transmisión del auto a agregar

TRANSMISSION = [
    ('A', 'Automatico'),
    ('M', 'Manual')
]

# Opciones para la selección del horario de la cita

SCHEDULE = [
    ('8:00 am', '8:00 am'),
    ('9:00 am', '9:00 am'),
    ('10:00 am', '10:00 am'),
    ('11:00 am', '11:00 am'),
    ('1:00 pm', '1:00 pm'),
    ('2:00 pm', '2:00 pm'),
    ('3:00 pm', '3:00 pm'),
    ('4:00 pm', '4:00 pm'),
]


# Modelo empleado para los objetos de tipo car que se utilizan para guardar
# las citas en la base de datos de sqlite3

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="car", null=True)

    provider = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="provider", null=True)

    car_model = models.CharField(max_length=20)
    transmission = models.CharField(max_length=1, choices=TRANSMISSION)
    year = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    schedule = models.CharField(max_length=10, choices=SCHEDULE)
    date = models.DateField(null=True, blank=False)
