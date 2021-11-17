from abc import ABC, abstractmethod

from buildings.build.buildings import *

from buildings.models import Buildings


class BuildingsCreator(ABC):
    @abstractmethod
    def create_building(self, buildings_bd: Buildings):
        pass


class ConcreteCastle(BuildingsCreator):
    def create_building(self, buildings_bd: Buildings) -> Castle:
        item = buildings_bd.objects.filter(name_building="Замок")[0]
        return Castle(item.name_building, item.building_level, item.building_health, item.stone, item.wood,
                      item.iron, item.size_warehouse, item.id_unit)


class ConcreteWarehouse(BuildingsCreator):
    def create_building(self, buildings_bd: Buildings) -> Castle:
        item = buildings_bd.objects.filter(name_building="Склад")[0]
        return Castle(item.name_building, item.building_level, item.building_health, item.stone, item.wood,
                      item.iron, item.size_warehouse, item.id_unit)
