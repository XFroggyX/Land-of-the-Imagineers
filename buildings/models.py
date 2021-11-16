from django.db import models


class Buildings(models.Model):
    name_building = models.CharField(max_length=30)
    building_level = models.PositiveSmallIntegerField()
    building_health = models.PositiveIntegerField()
    stone = models.PositiveSmallIntegerField()
    wood = models.PositiveSmallIntegerField()
    iron = models.PositiveSmallIntegerField()
    size_warehouse = models.PositiveIntegerField(null=True)
    id_unit = models.ForeignKey(
        'Units',
        on_delete=models.CASCADE,
        null=True,
    )


class Units(models.Model):
    pass
