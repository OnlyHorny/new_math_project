import pandas as pd


def get_password(conn, username):
    df = pd.read_sql(f'''SELECT password
FROM user WHERE login = '{username}';
''', conn)
    for row in df.itertuples():
        print(row)
        return row[1]


def update_userdata(conn, old_username, new_username, new_password):
    cur = conn.cursor()
    cur.execute(f'''UPDATE user
SET login = '{new_username}', password = '{new_password}'
WHERE login = '{old_username}';''')
    conn.commit()


def check_unique(conn, added_username):
    return len(pd.read_sql(f'''SELECT * FROM user
WHERE login = '{added_username}';''', conn)) == 0
