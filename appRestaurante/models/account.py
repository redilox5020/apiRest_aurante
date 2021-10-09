from django.db import models
from .user     import UserProfile
from .address  import Address
from .products import Product
# id, nombre, favoritos, compras, puntos por compra, domicilio
class Account(models.Model):
    id                = models.AutoField(primary_key=True)
    user              = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    #shopping          = models.ManyToManyField(Product) # relacion muchos a muchos
    favorite          = models.ManyToManyField(Product)
    pointsPerPurchase = models.IntegerField(default=0)
    address           = models.ForeignKey(Address, on_delete= models.SET_NULL, null=True)
    isActive          = models.BooleanField(default=True)

class AccountShopping(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    products_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Favorite(models.Model):
    products_id = models.ManyToManyField(Product) 
