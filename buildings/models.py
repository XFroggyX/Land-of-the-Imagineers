from django.db import models


class Building(models.Model):
    name_building = models.CharField(max_length=30)
    building_level = models.PositiveSmallIntegerField()
    building_health = models.PositiveIntegerField()
    stone = models.PositiveSmallIntegerField()
    wood = models.PositiveSmallIntegerField()
    iron = models.PositiveSmallIntegerField()
    size_warehouse = models.PositiveIntegerField(null=True)
    id_unit = models.ForeignKey(
        'Unit',
        on_delete=models.CASCADE,
        null=True,
    )


class Unit(models.Model):
    pass
