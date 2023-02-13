from abc import ABC, abstractmethod


class Skill(ABC):
    user = None
    target = None

    def __str__(self):
        return f'Умение {self.name}'

    def __repr__(self):
        return f'Skill {self.name} (stamina {self.stamina}, damage {self.damage})'

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        """Уменьшить выносливость атакующего и здоровье атакуемого после применения умения."""
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage

        return f'{self.user} использует {self} и наносит {self.damage} урона сопернику.'

    def _is_stamina_enough(self) -> bool:
        """Проверка, достаточно ли выносливости у игрока для применения умения."""
        return self.user.stamina >= self.stamina

    def use(self, user, target) -> str:
        """Использовать умение."""
        self.user = user
        self.target = target

        if self._is_stamina_enough:
            return self.skill_effect()

        return f"{self.user} попытался использовать {self} но у него не хватило выносливости."
