import pandas as pd


def check_username(conn, login):
    df = pd.read_sql(f'''
    SELECT * FROM userdata
    WHERE login = '{login}';
''', conn)
    return df.size > 0


def insert_user(conn, login, password):
    cur = conn.cursor()
    cur.execute(f'''
    INSERT INTO userdata
    (login, password)
    VALUES ('{login}', '{password}');
''')
    conn.commit()
