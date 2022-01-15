import sys

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions, mixins, status
from rest_framework.decorators import action, api_view
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from towns.models import Town
from towns.serializers import TownSerializer
from towns.town.town import get_struct_town, edit_struct_town
from .forms import UsersRegisterForm
from .models import UsersOfTown
from .serializers import UsersOfTownSerializer, TownStructSerializer, UserSerializer


def login_page(request):
    user = request.user
    if user.is_authenticated:
        return redirect("/town")
    if request.method == "GET":
        pass
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/town")

    return render(request, 'login.html', dict())


def main_page(request):
    user = request.user
    if user.is_authenticated:
        print("мы на главной странице")
        return render(request, 'main_page.html', dict())
    else:
        return redirect("/login")


def sign_up(request):
    if request.method == 'POST':
        form = UsersRegisterForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email already registered")
        else:
            if form.is_valid():
                instance = form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password2']
                email = form.cleaned_data['email']
                user = authenticate(username=username, password=password, email=email)
                instance.email = email
                instance.save()
                form.save_m2m()
                messages.success(request, f'You account has been created! How you can login')
                return redirect('/login')
    else:
        form = UsersRegisterForm()
    context = {'form': form}
    return render(request, 'sign_up_page.html', context)


class TownViewSet(viewsets.ModelViewSet):
    queryset = Town.objects.all().order_by('id')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TownSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


my_town = {"id": 1, "townName": "HappyTown", "wood": 30, "iron": 23, "stone": 56, "points": {
    1: {
        "nameBuild": "Замок",
        "lvl": 2
    },
    2: {},
    3: {}
}
           }


class StructTownViewSet(viewsets.ViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    def list(self, request):
        return Response({"error": "Миха, укажи id города"})

    def retrieve(self, request, *args, **kwargs):  # kwargs - параметр подходит для get
        return Response(get_struct_town(kwargs['pk']))

    @action(detail=True, methods=['post'])
    def edit_town(self, request, pk=None):
        serializer = TownStructSerializer(data=request.data)
        if serializer.is_valid():
            return Response(edit_struct_town(pk, request.data))
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


new = {
    "UsersID": 1,
    "TownsID": 1
}


def edit_user_town(data: dict) -> str:
    if not User.objects.filter(id=data["UsersID"]) or not Town.objects.filter(id=data["TownsID"]):
        return "User or Town are used"
    else:
        user_obj = User.objects.get(id=data["UsersID"])
        town_obj = Town.objects.get(id=data["TownsID"])
        user_town = UsersOfTown()
        user_town.UsersID = user_obj
        user_town.TownsID = town_obj
        user_town.save()

    return "Ok"


class UserListViewSet(viewsets.ViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    def list(self, request):
        queryset = UsersOfTown.objects.all().order_by('id')
        return Response(UsersOfTownSerializer(queryset, many=True).data)

    @action(detail=True, methods=['post'])
    def edit_user_town(self, request, pk=None):
        serializer = UsersOfTownSerializer(data=request.data)
        if serializer.is_valid():
            return Response(edit_user_town(request.data))
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    # queryset = UsersOfTown.objects.all().order_by('id')
    # serializer_class = UsersOfTownSerializer(queryset, many=True)


@api_view(['POST'])
def create_town(request, x, y, form=None):
    pass


@api_view(['GET', 'POST'])
def towns_list(request, format=None):
    if request.method == 'GET':
        town = Town.objects.all()
        serializer = TownSerializer(town, many=True)
        return Response(serializer.data)
    """
    elif request.method == 'POST':
        serializer = TownSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """


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


@api_view(['GET', 'POST'])
def users_towns_list(request, format=None):
    if request.method == 'GET':
        town_users = UsersOfTown.objects.all()
        serializer = UsersOfTownSerializer(town_users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UsersOfTownSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def current_user(request):
    if request.user.is_authenticated:
        id = request.user.id
        username = request.user.username
        return Response({'id': id, 'username': username})
    else:
        return Response({"error": "User not identified"})
