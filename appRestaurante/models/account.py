from django.db import models
from .user     import UserProfile
from .address  import Address
from .products import Product


# id, nombre, favoritos, compras, puntos por compra, domicilio
class Account(models.Model):
    id                = models.AutoField(primary_key=True)
    user              = models.ForeignKey(UserProfile,  related_name='account', on_delete=models.CASCADE)
    favorite          = models.ManyToManyField(Product, related_name='favorite', through= 'Detail_Favoritos')
    pointsPerPurchase = models.IntegerField(default=0)
    address           = models.ForeignKey(Address, on_delete= models.SET_NULL, null=True)
    isActive          = models.BooleanField(default=True)

class Orders(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    shopping= models.ManyToManyField(Product, through='Detail_Product')
    amount  = models.FloatField(default=0) # monto
    date    = models.DateField(auto_now_add=True)
    status  = models.BooleanField(default=False)


class Detail_Product(models.Model):
    orders      = models.ForeignKey(Orders, on_delete=models.CASCADE)
    products    = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=1)
    price       = models.FloatField(default=0) # el precio depende de la cantidad
    date        = models.DateField(auto_now_add=True)

class Detail_Favoritos(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date    = models.DateField(auto_now_add=True)
    status  = models.BooleanField(default=True)



