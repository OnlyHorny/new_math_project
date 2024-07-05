from app import app
from flask import render_template, redirect, url_for, flash, request, session
from models.auth_model import check_auth
from utils import get_db_connection


@app.route('/auth', methods=["POST", "GET"])
def auth():
    conn = get_db_connection()
    if request.method == "POST":
        print(request.form)
        username = request.form['username']
        password = request.form['password']
        if 'reg' in request.form.keys():
            return redirect(url_for('reg'))
        if check_auth(conn, username, password) and 'login' in request.form.keys():
            session['is_auth'] = True
            session['username'] = username
            return redirect(url_for('main_page'))
        else:
            flash('Имя пользователя или пароль указаны неверно:(')
            session['is_auth'] = False

    html = render_template("login form/auth.html",
                           is_auth=session.get('is_auth'))
    return html
