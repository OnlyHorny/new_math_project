import sqlite3


def get_db_connection():
    path = 'identifier.sqlite'
    return sqlite3.connect(path)
