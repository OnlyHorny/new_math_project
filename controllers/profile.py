from app import app
from flask import render_template, session, redirect, url_for, request, flash
from models.profile_model import get_password, update_userdata, check_unique, get_id_profile_student, \
    get_id_profile_teacher, get_data_profile_student, get_data_profile_teacher, get_list_users
from models.main_page_model import get_profile
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

    profileUser = get_profile(conn, session.get('username'))
    users = get_list_users(conn)

    if profileUser.to_string(header=False, index=False) == 'Admin':
        html = render_template('admin/profiles_edit.html',
                               url_for=url_for,
                               users=users)
        print(profileUser.to_string(header=False, index=False))
    else:
        if profileUser.to_string(header=False, index=False) == 'Teacher':
            id_profile = get_id_profile_teacher(conn, session.get('username'))
            DataProfile = get_data_profile_teacher(conn, id_profile.to_string(header=False, index=False))

            html = render_template('teacher/profile.html',
                                   profile_teacher=DataProfile.iloc[0].to_list(),
                                   url_for=url_for)
            print(profileUser.to_string(header=False, index=False) + '2')
        else:
            if profileUser.to_string(header=False, index=False) == 'Student':
                id_profile = get_id_profile_student(conn, session.get('username'))
                DataProfile = get_data_profile_student(conn, id_profile.to_string(header=False, index=False))
                html = render_template('student/profile.html',
                                       profile_student=DataProfile.iloc[0].to_list(),
                                       url_for=url_for)
                print(profileUser.to_string(header=False, index=False) + '3')
    return html
