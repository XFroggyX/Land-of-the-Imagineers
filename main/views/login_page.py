from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def login_page(request):
    user = request.user
    if user.is_authenticated:
        return redirect("/main")
    if request.method == "GET":
        pass
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass"]
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/main")

    return render(request, 'login.html', dict())
