import sqlite3


def get_db_connection():
    path = 'Lessons.db'
    return sqlite3.connect(path)
