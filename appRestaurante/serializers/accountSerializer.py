from appRestaurante.models.account import Account
from rest_framework import serializers
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['shopping', 'favorite','pointsPerPurchase','address', 'isActive']