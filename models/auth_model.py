import pandas as pd


def check_auth(conn, username, password):
    df = pd.read_sql(f'''
    SELECT * FROM user
    WHERE login = '{username}' AND password = '{password}';
    ''', conn)
    return df.size > 0
