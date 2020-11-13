from django.db import models
from django.contrib.auth.models import User
# Create your models here.

TRANSMISSION = [
    ('A', 'Automatico'),
    ('M', 'Manual')
]

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

DAYS = [
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miércoles', 'Miércoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
]

class Car(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="car", null=True)
    provider = models.ForeignKey(User,on_delete=models.CASCADE,related_name="provider", null=True)
    car_model = models.CharField(max_length=20)
    transmission = models.CharField(max_length=1, choices=TRANSMISSION)
    year = models.PositiveIntegerField(blank=True)
    brand =  models.CharField(max_length=20)
    day = models.CharField(max_length=10, choices=DAYS)
    schedule = models.CharField(max_length=10, choices=SCHEDULE)
    date = models.DateField(null=True, blank=False)
