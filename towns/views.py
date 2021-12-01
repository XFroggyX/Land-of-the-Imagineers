from django.shortcuts import render
from django.http import HttpResponse

from towns.town.town import *
from towns.models import Towns, PointsTownsBuildings, PointsTown
from buildings.models import Buildings


# Create your views here.

def index(request):
    t = Town(Towns, PointsTown, Buildings, PointsTownsBuildings)
    t.set_town_name("Город1")
    t.set_coordinates(1, 5)
    t.save_town()

    s = Town(Towns, PointsTown, Buildings, PointsTownsBuildings, id_town=8)
    print(s.get_town_name())
    print(s.space_in_town())
    print(s.list_buildings())
    s.place_building(5, 3)
    s.place_building(7, 4)
    print(s.space_in_town())
    s.delete_building(5)
    print(s.space_in_town())

    return HttpResponse("Town")