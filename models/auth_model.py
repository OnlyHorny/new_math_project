import pandas as pd


def check_auth(conn, login, password):
    df = pd.read_sql(f'''
    SELECT * FROM userdata
    WHERE login = '{login}' AND password = '{password}';
    ''', conn)
    return df.size > 0
