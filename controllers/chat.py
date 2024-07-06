from utils import get_db_connection
from app import app
from flask import request, redirect, url_for, render_template, session
from models.chat_model import list_teacher, list_student
from models.main_page_model import get_name_fio, get_profile
import sys


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
    teachers = list_teacher(conn)
    students = list_student(conn)
    profile = get_profile(conn, session.get('username'))
    if profile.to_string(header=False, index=False) == 'Teacher':
        html = render_template('teacher/chat.html',
                               student_name=student_name,
                               students=students)
    else:
        html = render_template('student/chat.html',
                               student_name=student_name,
                               teachers=teachers)
    return html
