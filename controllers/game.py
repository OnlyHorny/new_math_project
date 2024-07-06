from app import app
from flask import render_template, session, redirect, url_for, request, flash
from models.main_page_model import get_profile
from utils import get_db_connection


@app.route('/game')
def game():
    conn = get_db_connection()

    profile = get_profile(conn, session.get('username'))
    if profile.to_string(header=False, index=False) == 'Admin':
        html = render_template('admin/game.html')
        if profile.to_string(header=False, index=False) == 'Teacher':
            html = render_template('teacher/game.html')
    else:
        html = render_template('student/game.html')
    return html
