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
            session.clear()
            # clear session if the player failed a game before
            session['name'] = name
            # saves the input as the username
            game_map.create()
            # creates the map for the game
            session['map'] = game_map.names
            session['current'] = game_map.newmap[0].enter()
            # saves the current map and the current scene
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
            playerChoice = game_map.newmap[0].choice(command)
            # returns the value next or die
            if playerChoice == 'die':
                # clear the player session and then shows the death message
                session.clear()
                session['message'] = game_map.newmap[0].message
                return render_template('rooms/death.html')
            elif playerChoice == 'next':
                # moves the player to the next scene and then display the message
                session['command'] = command
                session['message'] = game_map.newmap[0].message
                game_map.newmap.pop(0)
                if len(game_map.newmap) == 0:
                    # checks if there are any more rooms left
                    return render_template('rooms/win.html')
                session['current'] = game_map.newmap[0].enter()

                return redirect(url_for('rooms.firstRoom'))
            elif playerChoice == 'help':
                return render_template('rooms/help.html')
            else:
                error = 'invalid command'

        flash(error)

    return render_template('rooms/game.html')
