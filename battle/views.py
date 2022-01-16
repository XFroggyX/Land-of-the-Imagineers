import sys

from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from battle.battle.fight import record_battle_in_db, get_all_battle_result
from battle.serializers import BattleStructSerializer

b = {"attacking": 0, "defending": 1}


def fight(id1, id2):
    return [1, 2]


class BattleListViewSet(viewsets.ViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    @action(detail=False, methods=['post'])
    def start_battle(self, request):
        winUser, loser = fight(0, 1)
        data = request.data
        record_battle_in_db(data["attacking"], data["defending"], winUser)
        return Response({"result": "ok"})

    @action(detail=True, methods=['get'])
    def get_result_battle(self, request, pk=None):
        data = get_all_battle_result(pk)
        return Response(BattleStructSerializer(data, many=True).data)
