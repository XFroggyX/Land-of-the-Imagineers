from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField("Название города", max_length=200)
