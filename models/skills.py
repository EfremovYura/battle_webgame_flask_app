from models.base.skill import Skill


class FuryPunch(Skill):
    name = 'Свирепый пинок'
    stamina = 6
    damage = 12

    def skill_effect(self) -> str:
        """Применить умение."""
        return super().skill_effect()


class HardShot(Skill):
    name = 'Мощный укол'
    stamina = 5
    damage = 15

    def skill_effect(self) -> str:
        """Применить умение."""
        return super().skill_effect()
