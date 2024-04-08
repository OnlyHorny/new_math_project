import pandas as pd


def get_lesson(conn, id):
    return pd.read_sql(f'''
SELECT * FROM Lessons WHERE ID_lessons == {id};''', conn)


def get_all_lessons(conn):
    return pd.read_sql(f'''SELECT * FROM Lessons;''', conn)
