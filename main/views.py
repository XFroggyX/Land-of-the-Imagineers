from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from towns.models import Town
from .forms import UsersRegisterForm
from .serializers import TownSerializer


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


class TownCreateView(viewsets.ModelViewSet):
    queryset = Town.objects.all().order_by('id')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TownSerializer


        
