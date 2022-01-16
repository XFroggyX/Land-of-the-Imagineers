from django.db import models

from buildings.models import Building

from units.models import Unit


class Town(models.Model):
    name_town = models.CharField(max_length=50)
    point_x = models.IntegerField()
    point_y = models.IntegerField()
    stone = models.PositiveIntegerField(default=0)
    wood = models.PositiveIntegerField(default=0)
    iron = models.PositiveIntegerField(default=0)


class PointsTown(models.Model):
    point_x = models.IntegerField()
    point_y = models.IntegerField()


class PointsTownsBuilding(models.Model):
    id_point_town = models.ForeignKey(PointsTown, on_delete=models.CASCADE, )
    id_building = models.ForeignKey(Building, on_delete=models.CASCADE, )
    id_town = models.ForeignKey(Town, on_delete=models.CASCADE, )


class TownUnit(models.Model):
    id_town = models.ForeignKey(Town, on_delete=models.CASCADE, )
    id_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, )
    count_units = models.PositiveIntegerField()
