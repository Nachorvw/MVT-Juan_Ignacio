from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    dni = models.IntegerField(unique=True,null=False)
    alive = models.BooleanField()

    def __str__(self):
        return self.name
