from app import app
from flask import request, redirect, url_for, render_template, flash
from models.reg_model import check_username, insert_user
from utils import get_db_connection


@app.route('/reg', methods=["POST", "GET"])
def reg():
    conn = get_db_connection()
    is_successful = True
    if request.method == "POST":
        if 'reg' in request.form.keys():
            username = request.form['username']
            password = request.form['password']
            if password != request.form['repeat_password']:
                is_successful = False
                flash('Пароли не совпадают.')
            elif check_username(conn, username):
                is_successful = False
                flash('Данный логин уже занят.')
            else:
                insert_user(conn, username, password)
                return redirect(url_for('auth'))
        else:
            return redirect(url_for('auth'))


    html = render_template('login form/reg.html',
                           is_successful=is_successful)
    return html
