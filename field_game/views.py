import sys

from django.shortcuts import render

from buildings.models import Building
from towns.models import PointsTown
from units.models import Unit


def gen_point_town(size_town):
    town_point = PointsTown.objects.all()
    if len(town_point) == size_town:
        return
    else:
        for i in range(size_town - len(town_point)):
            obj = PointsTown()
            obj.point_x = i
            obj.point_y = i + 1
            obj.save()


def gen_build_town(builds):
    for key, value in builds.items():
        if Building.objects.filter(name_building=key):
            continue
        obj = Building()
        obj.name_building = key
        obj.building_level = value['building_level']
        obj.building_health = value['building_health']
        obj.stone = value['stone']
        obj.wood = value['wood']
        obj.iron = value['iron']
        obj.size_warehouse = value['size_warehouse']
        obj.save()


def gen_unit(units):
    for key, value in units.items():
        if Unit.objects.filter(name_unit=key):
            continue
        obj = Unit()
        obj.name_unit = key
        obj.unit_level = value['unit_level']
        obj.unit_health = value['unit_health']
        obj.unit_attack = value['unit_attack']
        obj.save()

def display_field(request):
    gen_point_town(6)
    builds = {}
    builds["Замок"] = {'building_level': 1, 'building_health': 200, 'stone': 5, 'wood': 10, 'iron': 4,
                       'size_warehouse': 100}
    builds["Казармы"] = {'building_level': 1, 'building_health': 100, 'stone': 6, 'wood': 7, 'iron': 4,
                         'size_warehouse': 40}
    builds["Склад"] = {'building_level': 1, 'building_health': 50, 'stone': 5, 'wood': 8, 'iron': 4,
                       'size_warehouse' : 30}

    units = {}
    units["Воин"] = {'unit_level': 1, 'unit_health': 10, 'unit_attack': 4}
    gen_unit(units)

    gen_build_town(builds)
    return render(request, 'field.html')

def display_town(request):
    return render(request, 'town.html')
