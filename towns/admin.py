from django.contrib import admin

from .models import Town, PointsTown, PointsTownsBuilding


class TownsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_town', 'point_x', 'point_y')  # поля, которые мы видем в списке
    list_display_links = ('id', 'name_town')
    search_fields = ('id', 'name_town', 'point_x', 'point_y')


admin.site.register(Town, TownsAdmin)
admin.site.register(PointsTown)
admin.site.register(PointsTownsBuilding)
