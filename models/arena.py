import random

from models.base.basesingleton import BaseSingleton
from models.units import PlayerUnit, EnemyUnit


class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False
    battle_result = None

    def start_game(self, player: PlayerUnit, enemy: EnemyUnit) -> None:
        """Начать игру."""
        self.player = player
        self.enemy = enemy
        self.game_is_running = True

    @staticmethod
    def _format_result(result: str, turn_result: str) -> str:
        """Форматировать результат хода."""
        return f'-> {result} <br>' \
               f'<- {turn_result}'

    def _check_units_hp(self) -> None:
        """Проверить здоровье."""
        if self.player.hp > 0 and self.enemy.hp > 0:
            return None

        self._end_game()

    def get_battle_result(self) -> None:
        if self.player.hp <= 0 and self.enemy.hp <= 0:
            self.battle_result = 'Ничья.'
        elif self.player.hp <= 0:
            self.battle_result = 'Противник победил.'
        else:
            self.battle_result = 'Игрок победил.'

    def _stamina_regeneration(self) -> None:
        """Регенерация здоровья и выносливости для игрока и врага за ход."""
        for unit in (self.player, self.enemy):
            if unit.stamina + self.STAMINA_PER_ROUND > unit.unit_class.max_stamina:
                unit.stamina = unit.unit_class.max_stamina
            else:
                unit.stamina += self.STAMINA_PER_ROUND

    def next_turn(self) -> None:
        """По окончании хода проверить здоровье и восстановить выносливость."""
        self._check_units_hp()

        if self.game_is_running:
            self._stamina_regeneration()

    def _end_game(self) -> None:
        """Завершить игру."""
        self._instances = {}
        self.game_is_running = False

    def player_hit(self) -> None:
        """Нанести удар."""
        player_result = self.player.hit(self.enemy)
        enemy_result = self.enemy_action()
        self.battle_result = self._format_result(player_result, enemy_result)

    def player_use_skill(self) -> None:
        """Использовать умение."""
        player_result = self.player.use_skill(self.enemy)
        enemy_result = self.enemy_action()
        self.battle_result = self._format_result(player_result, enemy_result)

    def player_pass_turn(self) -> None:
        """Пользователь пропускает ход."""
        player_result = self.player.pass_turn()
        enemy_result = self.enemy_action()
        self.battle_result = self._format_result(player_result, enemy_result)

    def enemy_action(self) -> str:
        """Рандомный выбор действия противника."""
        actions = {
            'hit': self.enemy.hit,
            'use_skill': self.enemy.use_skill,
            'pass_turn': self.enemy.pass_turn
        }

        # С вероятностью 10% выбирается 'use_skill' или 'pass_turn'
        actions_list = ['hit'] * 8 + ['use_skill', 'pass_turn']
        action_to_do = random.choice(actions_list)
        enemy_result = actions.get(action_to_do)(self.player)

        self.next_turn()

        return enemy_result
