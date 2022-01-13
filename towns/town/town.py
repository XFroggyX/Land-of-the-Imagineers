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
            self.wood = item.wood
            self.iron = item.iron
            self.stone = item.stone

        else:
            self.town_name = ""
            self.point_x = None
            self.point_y = None
            self.id = None

        self.count_space = self.count_space_point()  # Количество мест для зданий

    def set_town_name(self, town_name_: str) -> str:
        item = self.towns_db.objects.filter(name_town=town_name_)
        if not item:
            self.town_name = town_name_
            return self.town_name
        else:
            return "The name of the town is occupied"

    def get_id(self) -> int:
        return self.id

    def get_wood(self):
        return self.wood

    def get_iron(self):
        return self.iron

    def get_stone(self):
        return self.stone

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

    def struct_town(self) -> dict:
        townStruct = {
            "id": self.id,
            "townName": self.town_name,
            "wood": self.wood,
            "iron": self.iron,
            "stone": self.stone,
            "points": self.places_builds()
        }

        return townStruct

    # Количество мест для зданий в городе
    def count_space_point(self) -> int:
        count_points = len(self.points_db.objects.annotate(Count('id')))
        return count_points

    # place_building - используется для постройки сданий в городе
    def place_building(self, point_id, building_id) -> None:
        points_obj = self.points_db.objects.get(id=point_id)
        building_obj = self.building_db.objects.get(id=building_id)
        town_obj = self.towns_db.objects.get(id=self.id)
        town = self.ptb_db()
        town.id_point_town = points_obj
        town.id_building = building_obj
        town.id_town = town_obj
        town.save()

    # list_buildings - возвращает список возможных для постройки зданий
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

    # places_builds - расположение объектов в городе
    def places_builds(self) -> dict:
        item = self.ptb_db.objects.filter(id_town=self.id).order_by('id_point_town')
        space = {i + 1: {} for i in range(self.count_space)}
        for i in range(len(item)):
            point_id = item[i].id_point_town.id
            space[point_id]["nameBuild"] = item[i].id_building.name_building
            space[point_id]["lvl"] = item[i].id_building.building_level
        return space


def create_town(town_name, x, y) -> None:
    town = Town(Towns, PointsTown, Buildings, PointsTownsBuildings)
    town.set_town_name(town_name)
    town.set_coordinates(x, y)
    town.save_town()


def get_town_obj(id_town) -> Town:
    return Town(Towns, PointsTown, Buildings, PointsTownsBuildings, id_town=id_town)


def get_struct_town(id_town) -> dict:
    town = get_town_obj(id_town)
    return town.struct_town()
