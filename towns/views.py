from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .town.town import *
from rest_framework import status, generics

from .models import Town
from rest_framework import viewsets, permissions
from .serializers import TownSerializer

# Create your views here.

"""
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
    
def index(request):
    return HttpResponse("Town")



class TownViewSet(viewsets.ModelViewSet):
    queryset = Town.objects.all().order_by('id')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TownSerializer


@api_view(['GET', 'POST'])
def towns_list(request, format=None):
    if request.method == 'GET':
        town = Town.objects.all()
        serializer = TownSerializer(town, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TownSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    try:
        town = Town.objects.get(pk=pk)
    except Town.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TownSerializer(town)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TownSerializer(town, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        town.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

"""
class TownCreateView(viewsets.ModelViewSet):
    queryset = Town.objects.all().order_by('id')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TownSerializer
    
"""


class TownViewSet(viewsets.ModelViewSet):
    queryset = Town.objects.all().order_by('id')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TownSerializer


@api_view(['GET'])
def user_count_view(request, format=None):
    """
    A view that returns the count of active users in JSON.
    """
    user_count = Town.objects.count()
    content = {'user_count': user_count}
    return Response(content)


def index(request):
    return HttpResponse("Town")
