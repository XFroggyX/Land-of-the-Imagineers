from django.shortcuts import render, redirect


def main_page(request):
    user = request.user
    if user.is_authenticated:
        print("мы на главной странице")
        return render(request, 'main_page.html', dict())
    else:
        return redirect("/login")
