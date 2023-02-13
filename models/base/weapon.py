from dataclasses import dataclass
from random import uniform


@dataclass
class Weapon:
    id: int
    name: str
    max_damage: float
    min_damage: float
    stamina_per_hit: float

    @property
    def damage(self) -> float:
        """Произвольное округленное значение урона из диапазона."""
        return round(uniform(self.min_damage, self.max_damage), 1)

    def __str__(self):
        return f'Оружие {self.name}'

    def __repr__(self):
        return f'Оружие {self.name} (потребляет {self.stamina_per_hit} выносливости атакующего, ' \
               f'наносит урон здоровью атакуемого от {self.min_damage} до {self.max_damage})'
