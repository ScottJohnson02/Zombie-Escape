import functools
from zombieEscape import map

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('rooms', __name__, url_prefix='/')
game_map = map.Map()


@bp.route('/', methods=('GET', 'POST'))
def start():
    session.clear()
    if request.method == 'POST':
        name = request.form['name']
        error = None

        if not name:
            error = 'Username is required.'

        if error is None:
            session['name'] = name
            print(game_map.names)
            print(game_map.scenes)
            print(game_map.newmap)
            game_map.create()
            print(game_map.names)
            print(game_map.scenes)
            print(game_map.newmap)
            session['map'] = game_map.names
            session['current'] = game_map.newmap[0].enter()
            print(game_map.newmap[0].enter())
            return redirect(url_for('rooms.firstRoom'))

        flash(error)

    return render_template('rooms/index.html')


@bp.route('/game', methods=('GET', 'POST'))
def firstRoom():

    if request.method == 'POST':
        command = request.form['command']
        error = None

        if not command:
            error = 'command is required.'

        if error is None:
            playerChoice = game_map.scenes[0].choice(command)

            print(game_map.scenes[0].choice(command))

            if playerChoice == 'die':
                session.clear()
                return render_template('rooms/death.html')
            elif playerChoice == 'next':
                session['command'] = command
                game_map.newmap.pop(0)
                if len(game_map.newmap) == 0:
                    return render_template('rooms/win.html')
                session['current'] = game_map.newmap[0].enter()
                return redirect(url_for('rooms.firstRoom'))
            elif playerChoice == 'help':
                return render_template('rooms/help.html')
            else:
                error = 'invalid command'

        flash(error)

    return render_template('rooms/game.html')
