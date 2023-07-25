from flask import Flask, render_template, request, redirect, url_for

from models.arena import Arena
from models.units import PlayerUnit, EnemyUnit
from utils import get_data_for_choose_hero_form, save_unit_info

app = Flask(__name__, template_folder="templates")

heroes = {}

arena = Arena()


@app.route("/")
def menu_page():
    """Начать игру."""
    return render_template('index.html')


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    """Выбрать героя и его экипировку."""
    if request.method == 'GET':
        header = 'Выберите героя'
        return render_template('hero_choosing.html', result=get_data_for_choose_hero_form(header))

    if request.method == 'POST':
        heroes['player'] = save_unit_info(request, PlayerUnit)
        return redirect(url_for('choose_enemy'))


# Test
@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy():
    """Выбрать противника и его экипировку."""
    if request.method == 'GET':
        header = 'Выберите противника'
        return render_template('hero_choosing.html', result=get_data_for_choose_hero_form(header))

    if request.method == 'POST':
        heroes['enemy'] = save_unit_info(request, EnemyUnit)
        return redirect(url_for('start_fight'))


@app.route("/fight/start")
def start_fight():
    """Начало игры."""
    arena.start_game(player=heroes['player'], enemy=heroes['enemy'])
    arena.battle_result = 'Готов к бою!'
    return redirect(url_for('fight'))


@app.route("/fight/")
def fight():
    """Результат хода."""
    return render_template('fight.html', heroes=heroes, result=arena.battle_result)


@app.route("/fight/hit")
def hit():
    """Кнопка Нанести удар."""
    if arena.game_is_running:
        arena.player_hit()
    else:
        arena.get_battle_result()

    return redirect(url_for('fight'))


@app.route("/fight/use-skill")
def use_skill():
    """Кнопка Использовать умение."""
    if arena.game_is_running:
        arena.player_use_skill()
    else:
        arena.get_battle_result()

    return redirect(url_for('fight'))


@app.route("/fight/pass-turn")
def pass_turn():
    """Кнопка Пропустить ход."""
    if arena.game_is_running:
        arena.player_pass_turn()
    else:
        arena.get_battle_result()

    return redirect(url_for('fight'))


@app.route("/fight/end-fight")
def end_fight():
    """Кнопка Завершить бой."""
    return redirect(url_for('menu_page'))


if __name__ == "__main__":
    app.run()
