import functools
from zombieEscape import map

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('rooms', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def start():
    if request.method == 'POST':
        name = request.form['name']
        error = None

        if not name:
            error = 'Username is required.'

        if error is None:
            session['name'] = name
            g.user = name
            print(g.user)
            return redirect(url_for('rooms.firstRoom'))

        flash(error)

    return render_template('rooms/index.html')


@bp.route('/game', methods=('GET', 'POST'))
def firstRoom():
    game_map = map.Map()
    game_map.create()
    session['map'] = game_map.names
    session['current'] = game_map.scenes[0].enter()
    print(game_map.scenes[0].enter())
    print(session['name'])
    return render_template('rooms/game.html')
