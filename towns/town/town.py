from django.db.models import Count

from ..models import Town as Towns, PointsTownsBuilding as PointsTownsBuildings, PointsTown
from buildings.models import Building as Buildings


class Town:
    def __init__(self, towns_db, points_db, building_db, ptb_bd, id_town=None):
        self.towns_db = towns_db
        self.points_db = points_db
        self.building_db = building_db
        self.ptb_db = ptb_bd
        self.id = id_town

        if id_town is not None:
            item = towns_db.objects.filter(id=id_town)[0]
            self.town_name = item.name_town
            if self.town_name == "The name of the town is occupied":
                raise ValueError
            self.point_x = item.point_x
            self.point_y = item.point_y
        else:
            self.town_name = ""
            self.point_x = None
            self.point_y = None
            self.id = None

        self.count_space = self.count_space_point() + 1  # Количество мест для сданий

    def set_town_name(self, town_name_: str) -> str:
        item = self.towns_db.objects.filter(name_town=town_name_)
        if not item:
            self.town_name = town_name_
            return self.town_name
        else:
            return "The name of the town is occupied"

    def get_id(self) -> int:
        return self.id

    def get_town_name(self) -> str:
        return self.town_name

    def set_coordinates(self, x, y) -> None:
        self.point_x = x
        self.point_y = y

    def save_town(self) -> int:
        town = self.towns_db(
            name_town=self.town_name,
            point_x=self.point_x,
            point_y=self.point_y
        )
        town.save()
        self.id = town.id
        return town.id

    # Количество мест для зданий в городе
    def count_space_point(self) -> int:
        item = self.points_db.objects.annotate(num_point=Count('id'))
        return item[0].num_point + 1

    def place_building(self, point_id, building_id) -> None:
        points_obj = self.points_db.objects.filter(id=point_id)[0]
        building_obj = self.building_db.objects.filter(id=building_id)[0]
        town_obj = self.towns_db.objects.filter(id=self.id)[0]
        town = self.ptb_db(
            id_point_town=points_obj,
            id_building=building_obj,
            id_town=town_obj
        )
        town.save()

    def list_buildings(self) -> dict:
        item = self.building_db.objects.all()
        buildings_id = {}
        for i in range(len(item)):
            buildings_id[item[i].id] = item[i].name_building
        return buildings_id

    def delete_building(self, point_id) -> None:
        points_obj = self.points_db.objects.filter(id=point_id)[0]
        item = self.ptb_db.objects.filter(id_point_town=points_obj)
        if item:
            item.delete()

    # space_in_town - свободное место в городе
    def space_in_town(self) -> dict:
        item = self.ptb_db.objects.filter(id_town=self.id).order_by('id_point_town')
        space = {i + 1: "" for i in range(self.count_space + 1)}
        for i in range(len(item)):
            point_id = item[i].id_point_town.id
            space[point_id] = item[i].id_building.name_building
        return space


def create_town(town_name, x, y) -> None:
    town = Town(Towns, PointsTown, Buildings, PointsTownsBuildings)
    town.set_town_name(town_name)
    town.set_coordinates(x, y)
    town.save_town()


def get_town_obj(id_town) -> Town:
    return Town(Towns, PointsTown, Buildings, PointsTownsBuildings, id_town=id_town)
