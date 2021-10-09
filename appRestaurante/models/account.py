from django.db import models
from .user     import User
from .address  import Address
from .products import Product
# id, nombre, favoritos, compras, puntos por compra, domicilio
class Account(models.Model):
    id                = models.AutoField(primary_key=True)
    user              = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    shopping          = models.ManyToManyField(Product) # relacion muchos a muchos
    favorite          = models.ManyToManyField(Product)
    pointsPerPurchase = models.IntegerField(default=0)
    address           = models.ForeignKey(Address, on_delete= models.SET_NULL, null=True)
    isActive          = models.BooleanField(default=True)
