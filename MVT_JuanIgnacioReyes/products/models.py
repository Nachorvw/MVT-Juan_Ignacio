from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=50)
    cuantity  = models.IntegerField(null=False)
    price = models.FloatField()
    available = models.BooleanField()
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name