from .models import Town
from rest_framework import serializers


class TownSerializer(serializers.ModelSerializer):
    name_town = serializers.CharField(max_length=50)
    point_x = serializers.IntegerField()
    point_y = serializers.IntegerField()

    class Meta:
        model = Town
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        return Town.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name_town = validated_data.get('name_town', instance.name_town)
        instance.point_x = validated_data.get('point_x', instance.point_x)
        instance.point_y = validated_data.get('point_y', instance.point_y)
        instance.save()
        return instance

