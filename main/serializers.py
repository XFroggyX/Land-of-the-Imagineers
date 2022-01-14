import sys

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


class UsersOfTownSerializer(serializers.Serializer):
    UsersID = serializers.IntegerField(source='UsersID.id')
    TownsID = serializers.IntegerField(source='TownsID.id')

    class Meta:
        model = UsersOfTown
        fields = ['id', 'UsersID', 'TownsID']

    """
    def create(self, validated_data):
        sys.stdout.write(f"{validated_data}")
        data = {"UsersID": validated_data["UsersID"]['id'], "TownsID": validated_data["TownsID"]['id']}
        return UsersOfTown.objects.get_or_create(
            UsersID=User.objects.get(id=validated_data["UsersID"]['id']),
            TownsID=Town.objects.get(id=validated_data["TownsID"]['id'])
        )

    def update(self, instance, validated_data):
        instance.UsersID = validated_data.get('UsersID.id', instance.UsersID)
        instance.TownsID = validated_data.get('TownsID.id', instance.TownsID)
        instance.save()
        return instance
    """


class BuildsTownSerializer(serializers.Serializer):
    nameBuild = serializers.CharField(max_length=30)
    lvlBuild = serializers.IntegerField()


class PointsSerializer(serializers.Serializer):
    pointID = BuildsTownSerializer(required=False)


class TownStructSerializer(serializers.Serializer):
    townName = serializers.CharField(max_length=50)
    wood = serializers.IntegerField()
    iron = serializers.IntegerField()
    stone = serializers.IntegerField()
    points = PointsSerializer()

    class Meta:
        fields = ['email', 'username', 'password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'is_superuser', 'username')


"""
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
"""
