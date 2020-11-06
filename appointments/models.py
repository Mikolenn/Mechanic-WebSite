from django.db import models

# Create your models here.

TRANSMISSION = [
    ('A', 'Automatico'),
    ('M', 'Manual')
]


class Car(models.Model):
    car_model = models.CharField(max_length=20)
    transmission = models.CharField(max_length=1, choices=TRANSMISSION)
    year = models.PositiveIntegerField(blank=True)
    brand =  models.CharField(max_length=20)
