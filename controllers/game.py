from app import app


@app.route('/game')
def game():
    return 'student/game.html'
