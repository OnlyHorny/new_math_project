from app import app
from flask import request, redirect, url_for, render_template


@app.route('/')
def main_page():
    html = render_template('student/main_page.html')
    return html
