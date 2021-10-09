from appRestaurante.models.products import Product
from rest_framework import serializers
class productsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'