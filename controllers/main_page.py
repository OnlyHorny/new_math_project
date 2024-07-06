from app import app
from flask import request, redirect, url_for, render_template, session
from utils import get_db_connection
from models.main_page_model import get_all_lessons, get_lesson, get_name_fio, get_profile, get_dopTMaterial, \
    get_dopTMaterial_lesson
import sys


@app.route('/')
def main_page():
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
    content = get_lesson(conn, 1)
    lessons = get_all_lessons(conn)
    DopMaterial = get_dopTMaterial(conn)
    profile = get_profile(conn, session.get('username'))
    if profile.to_string(header=False, index=False) == 'Admin':
        html = render_template('admin/main_page.html',
                               student_name=student_name,
                               lessons=lessons,
                               DopMaterial=DopMaterial,
                               lesson_content=content.iloc[0].to_list())
        if profile.to_string(header=False, index=False) == 'Teacher':
            html = render_template('teacher/main_page.html',
                                   student_name=student_name,
                                   lessons=lessons,
                                   DopMaterial=DopMaterial,
                                   lesson_content=content.iloc[0].to_list())
    else:
        html = render_template('student/main_page.html',
                               student_name=student_name,
                               lessons=lessons,
                               DopMaterial=DopMaterial,
                               lesson_content=content.iloc[0].to_list())
    return html


@app.route('/<int:lesson_id>')
def lesson(lesson_id):
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

    content = get_lesson(conn, lesson_id)
    lessons = get_all_lessons(conn)
    DopMaterial = get_dopTMaterial(conn)

    profile = get_profile(conn, session.get('username'))
    if profile.to_string(header=False, index=False) == 'Admin':
        html = render_template('admin/main_page.html',
                               student_name=student_name,
                               lessons=lessons,
                               DopMaterial=DopMaterial,
                               lesson_content=content.iloc[0].to_list())
        if profile.to_string(header=False, index=False) == 'Teacher':
            html = render_template('teacher/main_page.html',
                                   student_name=student_name,
                                   lessons=lessons,
                                   DopMaterial=DopMaterial,
                                   lesson_content=content.iloc[0].to_list())
    else:
        html = render_template('student/main_page.html',
                               student_name=student_name,
                               lessons=lessons,
                               DopMaterial=DopMaterial,
                               contentDop=contentDop.iloc[0].to_list(),
                               lesson_content=content.iloc[0].to_list())
    return html
