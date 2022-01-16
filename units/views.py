from django.http import HttpResponse
from django.shortcuts import render

from abc import ABC, abstractmethod
from towns.models import TownUnit, Town
from units.models import Unit


def create_unit(unit_id, town_id):
    item = TownUnit.objects.filter(id_unit=unit_id, id_town=town_id)
    if not item:
        item = TownUnit.objects.create(id_unit=unit_id, id_town=town_id, count_units=1)
        item.save()
    else:
        item[0].count_units += 1
        item[0].save()
    return {"result": "ok"}


def index(request):
    A = Town.objects.get(id=1)
    B = Unit.objects.get(id=1)
    create_unit(B, A)
    return HttpResponse("Unit")
