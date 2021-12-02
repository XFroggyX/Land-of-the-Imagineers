from django.db import models


class Towns(models.Model):
    name_town = models.CharField(max_length=50)
    point_x = models.IntegerField()
    point_y = models.IntegerField()


class PointsTown(models.Model):
    point_x = models.IntegerField()
    point_y = models.IntegerField()


class PointsTownsBuildings(models.Model):
    id_point_town = models.ForeignKey('PointsTown', on_delete=models.CASCADE,)
    id_building = models.ForeignKey('buildings.Buildings', on_delete=models.CASCADE,)
    id_town = models.ForeignKey('Towns', on_delete=models.CASCADE,)