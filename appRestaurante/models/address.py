from django.db import models
class Address(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.CharField(max_length=255)
    barrio = models.CharField(max_length=255)

    def __str__(self):
        return f'Address {self.id}: {self.calle} {self.no_calle} {self.barrio}'