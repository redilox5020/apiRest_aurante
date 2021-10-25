from rest_framework import viewsets

from appRestaurante.models.account import Account, Orders
from appRestaurante.models.products import Ingredient, Recipe, Tag

from appRestaurante.serializers.accountSerializer import AccountListSerializer, OrdersSerializer
from appRestaurante.serializers.productsSerializer import IngredientSerializer, RecipeSerializer, TagSerializer

class AccountViewSet(viewsets.ModelViewSet):
    """ Crear y actualizar perfiles """
    # lo primero que se quiere es serializar la informacion 
    serializer_class = AccountListSerializer # llamamos nuestro serializador
    queryset = Account.objects.all() # Obtiene todos los objectos que existen

class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class IngredientsViewSet(viewsets.ModelViewSet):
    serializer_class= IngredientSerializer
    queryset = Ingredient.objects.all()

class TagsViewSet(viewsets.ModelViewSet):
    serializer_class= TagSerializer
    queryset = Tag.objects.all()