from app import app
from flask import render_template, session, redirect, url_for, request, flash
from models.profile_model import get_password, update_userdata, check_unique
from utils import get_db_connection

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    conn = get_db_connection()
    if 'is_auth' not in session or (not session['is_auth']):
        return redirect(url_for('auth'))
    if request.method == 'POST':
        if request.form['button'] == 'logout':
            session['is_auth'] = False
            del session['username']
            return redirect(url_for('main_page'))
        elif request.form['button'] == 'save':
            if check_unique(conn, request.form['new_username']):
                update_userdata(conn, session['username'], request.form['new_username'], request.form['password'])
                flash('Данные успешно изменены')
                session['username'] = request.form['new_username']
            else:
                flash('Данное имя пользователя уже занято')

    html = render_template('student/profile.html',
                           username=session.get('username'),
                           url_for=url_for,
                           password=get_password(conn, session['username']))
    return html
