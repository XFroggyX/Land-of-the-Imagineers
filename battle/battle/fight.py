import sys

from django.contrib.auth.models import User
import operator

from battle.models import Battle


def record_battle_in_db(attackingID, defendingID, winnerID):
    attacking_user_obj = User.objects.get(id=attackingID)
    defending_user_obj = User.objects.get(id=defendingID)
    result_user_obj = User.objects.get(id=winnerID)
    battle = Battle()
    battle.attackingID = attacking_user_obj
    battle.defendingID = defending_user_obj
    battle.result = result_user_obj
    battle.msgAttacking = 0
    battle.msgDefending = 0
    battle.save()


def get_all_battle_result(id):
    attack_battle = Battle.objects.filter(attackingID=id, msgAttacking=0).order_by('id')
    defend_battle = Battle.objects.filter(defendingID=id, msgDefending=0).order_by('id')
    all_battle = attack_battle | defend_battle
    all_battle = sorted(all_battle, key=operator.attrgetter('id'))

    for battle in attack_battle:
        up = Battle.objects.get(id=battle.id)
        up.msgAttacking = 1
        up.save()

    for battle in defend_battle:
        up = Battle.objects.get(id=battle.id)
        up.msgDefending = 1
        up.save()

    return all_battle
