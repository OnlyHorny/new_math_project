import pandas as pd


def check_username(conn, username):
    df = pd.read_sql(f'''
    SELECT * FROM User
    WHERE Login = '{username}';
''', conn)
    return df.size > 0


def insert_user(conn, username, password):
    cur = conn.cursor()
    cur.execute(f'''
    INSERT INTO User
    (Login, Password)
    VALUES ('{username}', '{password}');
''')
    conn.commit()
