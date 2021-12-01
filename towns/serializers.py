from towns.models import Towns
from rest_framework import serializers


class TownSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Towns
        fields = ('id', 'name_town', 'point_x', 'point_y')
