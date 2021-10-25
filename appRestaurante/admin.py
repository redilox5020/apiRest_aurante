from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _ # convierte cadenas de texto en texto legible para el humano
# Register your models here.
from django.contrib.admin.widgets import FilteredSelectMultiple
# se da acceso al administrador Para editar y crear

from .models.user    import UserProfile
from .models.account import Account, Detail_Favoritos, Detail_Product, Orders
from .models.address import Address
from .models.products import Images, Ingredient, Recipe, Tag

class DetailFavoritosInline(admin.TabularInline):
    model = Detail_Favoritos
    extra = 1
    autocomplete_fields = ['product']
    
class RecipeAdmin(admin.ModelAdmin):
    #inlines = [DetailFavoritosInline,]
    search_fields = ('title'),
    ordering = ['title']

class AcountAdmin(admin.ModelAdmin):
    inlines = [DetailFavoritosInline,]

class DetailProductInline(admin.TabularInline):
    model = Detail_Product
    extra = 1
    autocomplete_fields = ['products']
    
class OrdersAdmin(admin.ModelAdmin):
    inlines = [DetailProductInline,]

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = ( # son los campos que tenemos
    # Aqui definimos las secciones para nuestros filedsets, create, y change page
        # Cada uno de estos parentesis va ha ser una seccion
        #  el primer elmento va a ser el titulo de la seccion 
        #  el segundo elemento va a ser un diccionario con los campos
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields':('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    # Agregar usuarios desde el admin
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email', 'password1', 'password2')
        }),
    )

admin.site.register(UserProfile, UserAdmin)
admin.site.register(Account, AcountAdmin)
admin.site.register(Address)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Images)
