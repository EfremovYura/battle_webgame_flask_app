from dataclasses import dataclass


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float

    def __str__(self):
        return f'Броня {self.name}'

    def __repr__(self):
        return f'Armor {self.name} (stamina_per_turn {self.stamina_per_turn}, defence {self.defence})'
