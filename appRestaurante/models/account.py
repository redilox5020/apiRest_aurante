from django.db import models
from .user     import UserProfile
from .address  import Address
from .products import Recipe


# id, nombre, favoritos, compras, puntos por compra, domicilio
class Account(models.Model):
    id                = models.AutoField(primary_key=True)
    user              = models.ForeignKey(UserProfile,  related_name='account', on_delete=models.CASCADE)
    #shopping          = models.ManyToManyField(Product, through='AccountShopping') # relacion muchos a muchos
    # favorite          = models.ForeignKey(Favorite,     related_name='Favorite', on_delete=models.CASCADE)
    favorite          = models.ManyToManyField('Recipe', through='Detail_Favoritos', blank=True)
    pointsPerPurchase = models.IntegerField(default=0)
    address           = models.ForeignKey(Address, on_delete= models.SET_NULL, null=True)
    isActive          = models.BooleanField(default=True)

class Orders(models.Model):
    """ Pedidos por cuenta """
    STATUS_ORDER = (
        ('P', 'En Preparacion'),
        ('C', 'En Camino'),
        ('E', 'Entregado'),
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    shopping= models.ManyToManyField('Recipe', through='Detail_Product')
    amount  = models.FloatField(default=0) # monto
    date    = models.DateField(auto_now_add=True)
    status  = models.CharField(max_length=14, choices=STATUS_ORDER)


class Detail_Product(models.Model):
    orders      = models.ForeignKey(Orders, on_delete=models.CASCADE)
    products    = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=1)
    price       = models.FloatField(default=0) # el precio depende de la cantidad
    date        = models.DateField(auto_now_add=True)

class Detail_Favoritos(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date    = models.DateField(auto_now_add=True)
    status  = models.BooleanField(default=True)