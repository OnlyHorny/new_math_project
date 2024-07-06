import pandas as pd


def get_list_users(conn):
    return pd.read_sql(f''' 
    SELECT Login
    FROM User
    ;''', conn)


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


def get_id_profile_student(conn, user):
    return pd.read_sql(f''' 
    SELECT Id
    FROM student
    WHERE student.Login == '{user}'
    ;''', conn)


def get_id_profile_teacher(conn, user):
    return pd.read_sql(f''' 
    SELECT Id
    FROM teacher
    WHERE teacher.Login == '{user}'
    ;''', conn)


def get_data_profile_student(conn, Id):
    return pd.read_sql(f''' 
    SELECT Name, Name_univ, Curs, Mail, Login, Password
    FROM student
    LEFT JOIN Univ ON (student.Id_univ = Univ.Id_univ)
    WHERE student.Id == {Id}; ''', conn)


def get_data_profile_teacher(conn, Id):
    return pd.read_sql(f''' 
    SELECT Name, Name_univ, Name_step, Name_dol, Login, Password
    FROM teacher
    LEFT JOIN Univ ON (teacher.Id_univ = Univ.Id_univ)
    LEFT JOIN Step ON (teacher.Id_step = Step.Id_step)
    LEFT JOIN Dol ON (teacher.Id_dol = Dol.Id_dol)
    WHERE teacher.Id == {Id};''', conn)


