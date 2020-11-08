from django.db import models
from django.contrib.auth.models import User
# Create your models here.

TRANSMISSION = [
    ('A', 'Automatico'),
    ('M', 'Manual')
]


class Car(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="car", null=True)
    car_model = models.CharField(max_length=20)
    transmission = models.CharField(max_length=1, choices=TRANSMISSION)
    year = models.PositiveIntegerField(blank=True)
    brand =  models.CharField(max_length=20)



class ToDoList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="todolist", null=True)
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist=models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    complete=models.BooleanField()

    def __str__(self):
        return self.text
