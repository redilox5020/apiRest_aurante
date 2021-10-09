from django.db import models

class Product(models.Model):
    id                = models.AutoField(primary_key=True)
    nombre            = models.CharField(max_length = 50)
    precio            = models.IntegerField(default = 0 )
    tipo              = models.CharField(max_length = 50)
    marca             = models.CharField(max_length = 50, null= True)
    ingredientes      = models.CharField(max_length = 255, null=True)
