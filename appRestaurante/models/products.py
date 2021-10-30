from django.db import models
from django.conf import settings
import uuid
import os # manejador de rutas locales

def recipe_image_file_path(instance, filename):
    """ Genera path para imagenes """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/recipe/', filename)

class Recipe(models.Model):
    """ Receta objeto """
    user         = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title        = models.CharField(max_length=255)
    time_minutes = models.IntegerField()
    price        = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients  = models.ManyToManyField('Ingredient')
    tags         = models.ManyToManyField('Tag')
    slug         = models.SlugField()
    stock        = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Images(models.Model):
    """ Imagenes del la Preparacion """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    image  = models.ImageField(null=True, upload_to=recipe_image_file_path)
    def __str__(self) -> str:
        return f'Imagen Receta {self.recipe.title}'

class Tag(models.Model):
    """ Modelo del Tag para la receta """
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    def __str__(self) -> str:
        return self.name

class Ingredient(models.Model):
    """ Ingrediente para usarse en la receta """
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
