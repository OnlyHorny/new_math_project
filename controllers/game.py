from app import app
from flask import render_template, session, redirect, url_for, request, flash

from utils import get_db_connection

@app.route('/game')
def game():
    html = render_template('student/game.html')
    return html
