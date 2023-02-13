from models.base.baseunit import BaseUnit


class PlayerUnit(BaseUnit):
    def hit(self, target: BaseUnit) -> str:
        """Нанести удар сопернику."""
        return super().hit(target)

    def use_skill(self, target: BaseUnit) -> str:
        """Использовать умение."""
        if self._is_skill_used:
            return f'{self} уже использовал навык.' + ' ' + self.pass_turn()

        self._is_skill_used = True
        return self.unit_class.skill.use(self, target)


class EnemyUnit(BaseUnit):
    def hit(self, target: BaseUnit) -> str:
        """Соперник наносит удар."""
        return super().hit(target)

    def pass_turn(self, target: BaseUnit) -> str:
        """Пропустить ход."""
        return super().pass_turn()

    def use_skill(self, target: BaseUnit) -> str:
        """Использовать умение."""
        if self._is_skill_used:
            return f'{self} уже использовал навык.' + ' ' + self.hit(target)

        self._is_skill_used = True
        return self.unit_class.skill.use(self, target)
