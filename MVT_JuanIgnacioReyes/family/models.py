from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    birthdate = models.TimeField()
    dni = models.IntegerField(unique=True)
    alive = models.BooleanField()
