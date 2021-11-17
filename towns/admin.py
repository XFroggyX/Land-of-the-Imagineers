from django.contrib import admin

from .models import Towns, PointsTown, PointsTownsBuildings

admin.site.register(Towns)
admin.site.register(PointsTown)
admin.site.register(PointsTownsBuildings)
