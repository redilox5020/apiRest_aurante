from appRestaurante.models.account import Account, Orders
from rest_framework import serializers

from appRestaurante.models.products import Recipe
from appRestaurante.serializers.addressSerializer import AddressSerializer

class OrdersSerializer(serializers.ModelSerializer):
    """ Serializador para modelo de pedidos """
    
    shopping = serializers.PrimaryKeyRelatedField(
        many= True,
        queryset = Recipe.objects.all()
    )
    class Meta:
        model = Orders
        fields = ('id', 'shopping','amount', 'date','status',)
        read_only_fields = ('id',)

    def to_representation(self, obj):
        account = Account.objects.get(id=obj.id)
        favoritos = account.favorite.all()
        shopping = obj.shopping.all()
        return{

            'id': obj.id,
            'shopping': [s.__str__() for s in shopping],
            'account': {
                'id': account.id,
                'favorite': [p.__str__() for p in favoritos],
                'pointsPerPurchase' : account.pointsPerPurchase,
                'address': account.address.__str__(),
                'isActive': account.isActive
            },
            'amount': obj.amount,
            'date'  : obj.date,
            'status': obj.status,
        }

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pointsPerPurchase',  'isActive']

class AccountListSerializer(serializers.ModelSerializer):
    # address = serializers.StringRelatedField()
    favorite = serializers.PrimaryKeyRelatedField(
        many= True,
        queryset = Recipe.objects.all()
    )
    class Meta:
        model = Account
        fields = ['user','favorite','pointsPerPurchase', 'address', 'isActive']

    # def create(self, validated_data):
    #     ordersData = validated_data.pop('orders')
    #     accountInstance = Account.objects.create(**validated_data)
    #     Orders.objects.create(account=accountInstance, **ordersData)
    #     return accountInstance

    def to_representation(self, obj):

        favoritos = obj.favorite.all()
        return{
            'id': obj.id,
            'favorite': [p.__str__() for p in favoritos],
            'pointsPerPurchase' : obj.pointsPerPurchase,
            'address': obj.address.__str__(),
            'isActive': obj.isActive
        }