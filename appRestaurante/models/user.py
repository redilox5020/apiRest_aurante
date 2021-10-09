from django.db import models
from django.contrib.auth.models import AbstractBaseUser #modelo basico de Usuarios, Login con usuario
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

""" Dado que creo un modelos de usuario Personalizado, debo que especificar como procesar los usuarios """

class UserProfileManager(BaseUserManager):
    """ Manager para Perfiles de Usuario,
        la forma en que los manager funcionan es que especificas funciones para poder manipular los atributos de nuestros objetos de tipo UserProfile
    """
    
    def create_user(self,email,name,password=None): # no necesitas Password
        """ Crear nuevo perfil de Usuario """
        if not email:
            # en caso de no poner email, se envia un error
            raise ValueError('El Usuario debe tener un Email')
        
        email = self.normalize_email(email) # convierte el correo en la parte del dominio(lo que sigue despues de @) a minusculas
        user = self.model(email = email, name = name) # Definimos el Objeto de Usuario a partir del modelo heredado 

        user.set_password(password)

        # Asignamos el parametro using que hace referencia a cual bd vamos a usar, 
        # en este caso utilizamos la bd por defecto es decir la que configuramos en el settings
        user.save(using = self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email,name,password)

        user.is_superuser = True # se especifica automaticamente al heredar "PermissionsMixin" en el modelo Usuario
        user.is_staff = True # Es miembro del equipo
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Modelo Base de Datos para Usuarios en el Sistema"""
    email = models.EmailField(max_length=255, unique=True)
    #password = models.CharField('Password', max_length = 256)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # Si son Miembros del equipo
    
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'    #Campo de login que el usuario va especificar
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Obtener Nombre Completo del Usuario """
        return self.name

    def get_short_name(self): # en proceso
        """ Obtener Nombre Corto del Usuario """
        return self.name 

    def __str__(self): #Representacion en cadena de texto del Modelo
        """Retornar Cadena Representando Nuestro Usuario"""
        return self.email