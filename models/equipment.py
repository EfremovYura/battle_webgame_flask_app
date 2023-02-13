import json

import marshmallow_dataclass

from dataclasses import dataclass
from typing import Optional
from models.base.armor import Armor
from models.base.weapon import Weapon
from config import EQUIPMENT_FILE


@dataclass
class EquipmentData:
    weapons: list[Weapon]
    armors: list[Armor]


class Equipment:
    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name: str) -> Optional[Weapon]:
        """Возвращает объект оружия по имени."""
        for weapon in self.equipment.weapons:
            if weapon.name == weapon_name:
                return weapon
        return None

    def get_armor(self, armor_name: str) -> Optional[Armor]:
        """Возвращает объект брони по имени."""
        for armor in self.equipment.armors:
            if armor.name == armor_name:
                return armor
        return None

    def get_weapons_names(self) -> list[str]:
        """Возвращает список с названиями оружия."""
        return [weapon.name for weapon in self.equipment.weapons]

    def get_armors_names(self) -> list[str]:
        """Возвращает список с названиями брони."""
        return [armor.name for armor in self.equipment.armors]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        """Получает данные об экипировке из файла."""
        with open(EQUIPMENT_FILE, encoding='utf-8') as f:
            data = json.load(f)
            equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
            return equipment_schema().load(data)
