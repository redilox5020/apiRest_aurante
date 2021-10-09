from rest_framework                        import serializers
from appRestaurante.models.address import Address
from appRestaurante.models.user                   import User      # Traemos el modelo de Usuario
from appRestaurante.models.account                import Account   # Tambien Cuentas 
from appRestaurante.serializers.accountSerializer import AccountSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializa objeto de perfil de usuario """

    class Meta:
        model = User
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
        accountData = validated_data.pop('account')
        addressData = validated_data.pop('address')
        userInstance = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        Account.objects.create(user=userInstance, **accountData)
        Address.objects.create(**addressData)
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
        user = User.objects.get(id=obj.id)          # Se obtiene el Usuario a partir del id
        account = Account.objects.get(user=obj.id)  # Obtenemos la cuenta a partir del id de usuario
        address = Address.objects.get(account = account.id)
        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'account': {
                'id': account.id,
                'shopping': account.balance,
                'favorite': account.lastChangeDate,
                'pointsPerPurchase' : account.pointsPerPurchas,
                'address': {
                    'calle': address.calle,
                    'no_calle': address.no_calle,
                    'barrio': address.barrio
                },
                'isActive': account.isActive
            }
        }


