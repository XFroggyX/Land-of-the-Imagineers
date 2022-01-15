from django.shortcuts import render


# Create your views here.

def display_field(request):
    return render(request, 'field.html')

def display_town(request):
    return render(request, 'town.html')
