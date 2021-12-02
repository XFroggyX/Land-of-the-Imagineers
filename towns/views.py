from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from towns.town.town import *
from towns.models import Towns, PointsTownsBuildings, PointsTown
from buildings.models import Buildings
from towns.serializers import TownsSerializer
from rest_framework import viewsets, permissions, status

# Create your views here.

"""t = Town(Towns, PointsTown, Buildings, PointsTownsBuildings)
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
    
def index(request):
    return HttpResponse("Town")
"""


class TownViewSet(viewsets.ModelViewSet):
    queryset = Towns.objects.all().order_by('id')
    serializer_class = TownsSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET', 'POST'])
def towns_list(request, format=None):
    if request.method == 'GET':
        town = Towns.objects.all()
        serializer = TownsSerializer(town, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TownsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    try:
        town = Towns.objects.get(pk=pk)
    except Towns.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TownsSerializer(town)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TownsSerializer(town, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        town.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
