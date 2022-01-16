from django.shortcuts import render

from towns.models import PointsTown


def gen_point_town(size_town):
    town_point = PointsTown.objects.all()
    if len(town_point) == size_town:
        return
    else:
        for i in range(size_town - len(town_point)):
            obj = PointsTown()
            obj.point_x = i
            obj.point_y = i + 1
            obj.save()


def display_field(request):
    gen_point_town(6)
    return render(request, 'field.html')
