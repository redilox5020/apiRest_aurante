from django.contrib import admin

# Register your models here.

# se da acceso al administrador Para editar y crear

from .models.user    import UserProfile
from .models.account import Account
from .models.address import Address
from .models.products import Product
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Address)
admin.site.register(Product)
