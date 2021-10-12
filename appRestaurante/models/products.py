from django.db import models

class Product(models.Model):
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length = 50)
    price           = models.IntegerField(default = 0 )
    type            = models.CharField(max_length = 50)
    make            = models.CharField(max_length = 50, null= True)
    Description     = models.TextField()
    stock           = models.IntegerField(default=1)
    thumbnail       = models.ImageField()
    slug            = models.SlugField() # identificador por nombre del Producto en url
    publish_date    = models.DateTimeField(auto_now_add=True)
    last_updated    = models.DateTimeField(auto_now=True)
