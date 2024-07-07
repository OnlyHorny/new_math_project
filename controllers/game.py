from app import app
from flask import render_template


@app.route('/game')
def game():
    return render_template('game/index.html')
