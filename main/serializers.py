from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import UsersOfTown
from towns.models import Town

"""
class UsersOfTownSerializer(serializers.ModelSerializer):
    id_point_town = serializers.ReadOnlyField(source='id_point_town.point_x')
    id_building = serializers.ReadOnlyField(source='id_building.point_x')
    id_town = serializers.ReadOnlyField(source='id_town.name_town')

    class Meta:
        model = PointsTownsBuilding
        fields = "__all__"

"""


class UsersOfTownSerializer(serializers.ModelSerializer):
    UsersID = serializers.ReadOnlyField(source='UsersID.id')
    TownsID = serializers.ReadOnlyField(source='TownsID.id')

    class Meta:
        model = UsersOfTown
        fields = "__all__"


class TownSerializer(serializers.ModelSerializer):
    name_town = serializers.CharField(max_length=50)
    point_x = serializers.IntegerField()
    point_y = serializers.IntegerField()

    class Meta:
        model = Town
        fields = ('id', 'name_town', 'point_x', 'point_y')

    def create(self, validated_data):
        return Town.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name_town = validated_data.get('name_town', instance.name_town)
        instance.point_x = validated_data.get('point_x', instance.point_x)
        instance.point_y = validated_data.get('point_y', instance.point_y)
        instance.save()
        return instance
