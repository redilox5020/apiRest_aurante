from appRestaurante.models.products import Recipe, Tag, Ingredient, Images
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    """ Serializador para modelo de tag """
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)

class IngredientSerializer(serializers.ModelSerializer):
    """ Serializador para modelo de ingrediente """
    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)

class RecipeSerializer(serializers.ModelSerializer):
    """ Serializador para modelo de recetas """
    
    ingredients = serializers.PrimaryKeyRelatedField(
        many= True,
        queryset = Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset= Tag.objects.all()
    )
    
    class Meta:
        model = Recipe
        fields = ('id', 'title','ingredients','tags', 'time_minutes','price', 'stock')
        read_only_fields = ('id',)

class RecipeDetailSerializer(RecipeSerializer):
    """ Serializa los detalle de receta """
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

class RecipeImageSerializer(serializers.ModelSerializer):
    """ Serializa Imagenes """
    class Meta:
        model = Images
        fields = ('id', 'image')
        read_only_fields = ('id',)