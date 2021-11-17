from django.shortcuts import render
from django.http import HttpResponse

from buildings.build.create_buildings import *

from buildings.models import Buildings


# чтение и запись в бд
def test_import_castle_bd():
    name = "Замок"
    lvl = 1
    hp = 100
    stone = 10
    wood = 4
    iron = 3
    size = 200
    castle = Buildings(
        name_building=name,
        building_level=lvl,
        building_health=hp,
        stone=stone,
        wood=wood,
        iron=iron,
        size_warehouse=size
    )
    castle.save()

    get_castle = Buildings.objects.all()
    assert get_castle[0] == castle
    get_castle[0].delete()


def index(request):
    c = ConcreteCastle().create_building(Buildings)
    return HttpResponse(c.get_name())
