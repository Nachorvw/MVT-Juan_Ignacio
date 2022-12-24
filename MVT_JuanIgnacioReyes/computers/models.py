from django.db import models
# Create your models here.

class Computer(models.Model):
    serial_num = models.IntegerField(max_length=100, unique=True)
    usage = models.BooleanField()
    
