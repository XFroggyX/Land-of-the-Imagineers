from django.db import models


# Create your models here.
class Unit(models.Model):
    name_unit = models.CharField(max_length=30)
    unit_level = models.PositiveSmallIntegerField()
    unit_health = models.PositiveIntegerField()
    unit_attack = models.PositiveIntegerField()
