import sys

from django.contrib.auth.models import User
import operator

from battle.models import Battle
from towns.models import TownUnit, Town
from units.models import Unit
from main.models import UsersOfTown


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


def fight(attack_user_id, defender_user_id):
    power_a = 0
    power_d = 0
    attack_obj = UsersOfTown.objects.get(UsersID_id=attack_user_id)
    defender_obg = UsersOfTown.objects.get(UsersID_id=defender_user_id)
    attack_town_id = attack_obj.TownsID_id
    defender_town_id = defender_obg.TownsID_id
    attack_all_units = TownUnit.objects.filter(id_town_id=attack_town_id)
    defender_all_units = TownUnit.objects.filter(id_town_id=defender_town_id)
    for i in range(len(attack_all_units)):
        power_a += attack_all_units[i].count_units * Unit.objects.get(id=attack_all_units[i].id_unit_id).unit_attack
    for i in range(len(defender_all_units)):
        power_d += defender_all_units[i].count_units * Unit.objects.get(id=defender_all_units[i].id_unit_id).unit_attack
    if power_a > power_d:
        return [attack_user_id, defender_user_id]
    else:
        return [defender_user_id, attack_user_id]
