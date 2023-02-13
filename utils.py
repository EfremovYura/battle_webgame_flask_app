from __future__ import annotations

from models.base.baseunit import BaseUnit
from models.unitclasses import unit_classes
from models.equipment import Equipment
from flask import request


def get_data_for_choose_hero_form(header: str) -> dict:
    """Получить данные для формы выбора героя."""
    equipment = Equipment()
    weapons = equipment.get_weapons_names()
    armors = equipment.get_armors_names()
    result = {'header': header,
              'weapons': weapons,
              'armors': armors,
              'classes': unit_classes
              }
    return result


def save_unit_info(request_: request, new_unit: type[BaseUnit]) -> BaseUnit:
    """Сохранить выбранную экипировку игроку."""
    name = request_.form['name']
    weapon_name = request_.form['weapon']
    armor_name = request_.form['armor']
    unit_class = request_.form['unit_class']
    unit_object = new_unit(name=name, unit_class=unit_classes.get(unit_class))
    unit_object.equip_armor(Equipment().get_armor(armor_name))
    unit_object.equip_weapon(Equipment().get_weapon(weapon_name))
    return unit_object
