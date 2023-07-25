from dataclasses import dataclass
from models.base.skill import Skill


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill

    def __str__(self):
        return f'Класс {self.name}'

    def __repr__(self):
        return f'UnitClass {self.name} (max_health {self.max_health}, max_stamina {self.max_stamina}, ' \
               f'attack {self.attack}, stamina {self.stamina}, armor {self.armor}, skill {self.skill})'
