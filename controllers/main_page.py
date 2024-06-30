from app import app
from flask import request, redirect, url_for, render_template, session
from utils import get_db_connection
from models.main_page_model import get_all_lessons, get_lesson
import sys

@app.route('/')
def main_page():
    if 'is_auth' not in session:
        session['is_auth'] = False
    if session.get('username') != None:
        student_name = session.get('username')
    else:
        student_name = 'student'
    # student_name = session.get('username') if 'login' in session else 'student' #нужно исправить на вывод имени если оно есть
    conn = get_db_connection()
    content = get_lesson(conn, 1)
    lessons = get_all_lessons(conn)
    print(lessons, file=sys.stdout)
    html = render_template('student/main_page.html',
                           student_name=student_name,
                           lessons=lessons,
                           lesson_content=content.iloc[0].to_list())
    return html


@app.route('/<int:lesson_id>')
def lesson(lesson_id):
    student_name = session.get('username') if 'username' in session else 'student'
    conn = get_db_connection()
    content = get_lesson(conn, lesson_id)
    lessons = get_all_lessons(conn)
    html = render_template('student/main_page.html',
                           student_name=student_name,
                           lessons=lessons,
                           lesson_content=content.iloc[0].to_list())
    return html
