from rest_framework                        import serializers
from appRestaurante.models.address import Address
from appRestaurante.models.user                   import UserProfile      # Traemos el modelo de Usuario
from appRestaurante.models.account                import Account
from appRestaurante.serializers.accountSerializer import AccountSerializer
from appRestaurante.serializers.addressSerializer import AddressSerializer  # Tambien Cuentas 



class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializa objeto de perfil de usuario """
    account = AccountSerializer()
    address = AddressSerializer()
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password', 'account', 'address')

        ''' Se hace un excepcion con el campo de password ya que no se quiere ver el hash del password '''
        extra_kwargs = {
            'password': {
                # cuando ocurre password, se añaden permisos adicionales
                'write_only': True, # con esto impedimos que el password sea visible cuando se recupera el objeto, solo es visible cuando se esta creando
                'style': {'input_type': 'password'}# para estilizar la clave, no se muestra la info, a cambio se muestran *
            }
        }

    def create(self, validated_data):
        """ Crea y retornar nuevo usuario """
        
        accountData  = validated_data.pop('account')
        addressData  = validated_data.pop('address')
        print(validated_data)
        userInstance = UserProfile.objects.create(**validated_data) 
        userInstance.set_password(validated_data["password"])
        userInstance.save()

        addressInstance = Address.objects.create(**addressData)

        Account.objects.create(user=userInstance, address=addressInstance, **accountData)

        return userInstance


    def update(self, instance, validated_data):
        """ Actualiza cuenta de usuario """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)

        #Proceso de Serializacion - Objeto a JSON
    
    ''' Similar al toString en java, su funcion es representar la informacion 
    Emparejamiento directo entre la data que llega y la estructura del JSON que se espera '''
    def to_representation(self, obj):               # obj: cada uno de los objetos que llega de la consulta 
        print(obj)
        user = UserProfile.objects.get(id=obj.id)          # Se obtiene el Usuario a partir del id
        account = Account.objects.get(user=obj.id)  # Obtenemos la cuenta a partir del id de usuario
        address = Address.objects.get(id=obj.id)
        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'account': {
                #'id': account.id,
                # 'orders': account.shopping,
                # 'favorite': account.favorite,
                'pointsPerPurchase' : account.pointsPerPurchase,
                'address': address.__str__(),
                'isActive': account.isActive
            }
        }


