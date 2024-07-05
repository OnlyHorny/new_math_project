from app import app
from flask import request, redirect, url_for, render_template, session
from utils import get_db_connection
from models.chat_model import list_teacher
from models.main_page_model import get_name_fio

@app.route('/chat')
def chat():
    conn = get_db_connection()
    if 'is_auth' not in session:
        session['is_auth'] = False
    if session.get('username') is not None:
        if session.get('username') == 'admin':
            student_name = session.get('username')
        else:
            student_name = get_name_fio(conn, session.get('username'))
            student_name = student_name.to_string(header=False, index=False)
            if student_name == 'None':
                student_name = session.get('username')
    else:
        student_name = 'student'

        html = render_template('student/chat.html',

    return html