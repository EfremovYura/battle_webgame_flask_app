from __future__ import annotations
from abc import ABC, abstractmethod
from models.base.armor import Armor
from models.base.unitclass import UnitClass
from models.base.weapon import Weapon


class BaseUnit(ABC):
    def __init__(self, name: str, unit_class: UnitClass):
        self.name = name
        self.unit_class = unit_class
        self.hp = unit_class.max_health
        self.stamina = unit_class.max_stamina
        self.weapon = None
        self.armor = None
        self._is_skill_used = False

    def __str__(self):
        return f'{self.unit_class.name} {self.name}'

    def __repr__(self):
        return f'name {self.name} (unit_class {self.unit_class}, hp {self.hp}, stamina {self.stamina}, ' \
               f'armor {self.armor}, weapon {self.weapon})'

    @property
    def health_points(self) -> float:
        """Здоровье в округленном виде."""
        return round(self.hp, 1)

    @property
    def stamina_points(self) -> float:
        """Выносливость в округленном виде."""
        return round(self.stamina, 1)

    def equip_weapon(self, weapon: Weapon) -> None:
        """Вооружиться."""
        self.weapon = weapon

    def equip_armor(self, armor: Armor) -> None:
        """Одеть броню."""
        self.armor = armor

    def _count_damage(self, target: BaseUnit) -> float:
        """Функция подсчета наносимого урона здоровью и расхода выносливости."""
        self.stamina -= self.weapon.stamina_per_hit
        damage = self.weapon.damage * self.unit_class.attack

        if target.stamina >= target.armor.stamina_per_turn * target.unit_class.stamina:
            target.stamina -= target.armor.stamina_per_turn * target.unit_class.stamina
            damage -= target.armor.defence * target.unit_class.armor

        damage = round(damage, 1)
        target.apply_damage(damage)

        return damage

    def apply_damage(self, damage: int) -> None:
        if damage > 0:
            self.hp -= damage

        if self.hp < 0:
            self.hp = 0

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        """Применить оружие."""
        # Не хватило выносливости для использования оружия.
        if self.stamina < self.weapon.stamina_per_hit:
            return f"{self} попытался использовать {self.weapon}, но у него не хватило выносливости."

        damage = self._count_damage(target)

        # Пробивает броню
        if damage > 0:
            return f"{self}, используя {self.weapon}, наносит удар и пробивает {target.armor} у {target}. " \
                   f"Урон -{damage}."

        # Броня останавливает урон.
        return f"{self}, используя {self.weapon}, наносит удар, но {target.armor} у {target} его останавливает."

    def use_skill(self, target: BaseUnit) -> str:
        """Использовать умение."""
        if self._is_skill_used:
            return f'{self} уже использовал навык.'

        self._is_skill_used = True
        return self.unit_class.skill.use(self, target)

    def pass_turn(self) -> str:
        """Пропустить ход."""
        return f'{self} пропускает ход.'
