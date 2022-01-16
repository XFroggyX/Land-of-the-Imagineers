from abc import ABC, abstractmethod


class Buildings(ABC):

    @abstractmethod
    def __init__(self, buildings_bd):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_level(self) -> int:
        pass

    @abstractmethod
    def get_health_points(self) -> int:
        pass

    @abstractmethod
    def get_list_resources(self) -> dict:
        pass

    @abstractmethod
    def get_size_warehouse(self) -> str:
        pass


class Castle(Buildings):
    def __init__(self, name, level, health, stone, wood, iron, size_warehouse):
        self.name = name
        self.level = level
        self.health = health
        self.stone = stone
        self.wood = wood
        self.iron = iron
        self.size_warehouse = size_warehouse

    def get_name(self) -> str:
        return self.name

    def get_level(self) -> int:
        return self.level

    def get_health_points(self) -> int:
        return self.health

    def get_list_resources(self) -> dict:
        return {'stone': self.stone, 'wood': self.wood, 'iron': self.iron}

    def get_size_warehouse(self) -> str:
        return self.size_warehouse


class Warehouse(Buildings):
    def __init__(self, name, level, health, stone, wood, iron, size_warehouse):
        self.name = name
        self.level = level
        self.health = health
        self.stone = stone
        self.wood = wood
        self.iron = iron
        self.size_warehouse = size_warehouse

    def get_name(self) -> str:
        return self.name

    def get_level(self) -> int:
        return self.level

    def get_health_points(self) -> int:
        return self.health

    def get_list_resources(self) -> dict:
        return {'stone': self.stone, 'wood': self.wood, 'iron': self.iron}

    def get_size_warehouse(self) -> str:
        return self.size_warehouse


if __name__ == "__main__":
    pass
