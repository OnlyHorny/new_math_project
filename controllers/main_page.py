from app import app
from flask import request, redirect, url_for, render_template, session
from utils import get_db_connection
from models.main_page_model import get_all_lessons, get_lesson


@app.route('/')
def main_page():
    if 'is_auth' not in session:
        session['is_auth'] = False
    student_name = session.get('username') if 'username' in session else 'student'
    conn = get_db_connection()
    content = get_lesson(conn, 1)
    lessons = get_all_lessons(conn)
    html = render_template('student/main_page.html',
                           student_name=student_name,
                           lessons=lessons,
                           lesson_content=content.iloc[0].to_list())
    return html


@app.route('/<int:lesson_id>')
def lesson(lesson_id):
    conn = get_db_connection()
    content = get_lesson(conn, lesson_id)
    lessons = get_all_lessons(conn)
    html = render_template('student/main_page.html',
                           lessons=lessons,
                           lesson_content=content.iloc[0].to_list())
    return html
