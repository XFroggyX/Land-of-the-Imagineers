import sys

from rest_framework import serializers


class BattleStructSerializer(serializers.Serializer):
    attackingID = serializers.IntegerField(source='attackingID.id')
    defendingID = serializers.IntegerField(source='defendingID.id')
    result = serializers.IntegerField(source='result.id')
    msgAttacking = serializers.IntegerField(default=0)
    msgDefending = serializers.IntegerField(default=0)

    class Meta:
        fields = '__all__'
