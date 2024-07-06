from app import app
from flask import request, redirect, url_for, render_template, session
from utils import get_db_connection
from models.main_page_model import get_profile


@app.route('/LessonPush')
def LessonPush():
    conn = get_db_connection()

    profile = get_profile(conn, session.get('username'))
    if profile.to_string(header=False, index=False) == 'Teacher':
        html = render_template('teacher/lesson_request.html')
    return html
