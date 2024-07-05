import pandas as pd


def get_lesson(conn, id):
    return pd.read_sql(f'''
    SELECT Tema.Name_tema,
    TMaterial.Text,
        CASE WHEN PMaterial.Text IS NULL OR PMaterial.Text = '' THEN NULL ELSE PMaterial.Text END AS PMaterial_Text,
        CASE WHEN PMaterial.Difficulty IS NULL OR PMaterial.Difficulty = '' THEN NULL ELSE PMaterial.Difficulty END AS PMaterial_Difficulty
    FROM Course
    Join Tema on Course.Id_tema=Tema.Id_tema
    Join TMaterial on Course.Id_TMaterial=TMaterial.Id_TMaterial
    LEFT Join Test on Course.Id_test=Test.Id_test
    LEFT Join TestPMaterial
    on TestPMaterial.Id_test=Test.Id_test
    LEFT JOIN PMaterial
    on TestPMaterial.Id_PMaterial=PMaterial.Id_PMaterial
    WHERE ID_course == {id};''', conn)


def get_all_lessons(conn):
    return pd.read_sql(f'''SELECT Tema.Id_tema, Tema.Name_tema
    FROM Course
    Join Tema on Course.Id_tema=Tema.Id_tema;''', conn)


def get_name_fio(conn, user):
    return pd.read_sql(
        f'''SELECT 
    CASE
        WHEN User.Profile = 'Student' THEN student.Name
        WHEN User.Profile = 'Teacher'  THEN teacher.Name
    END as Name
    FROM User
LEFT JOIN student ON (User.Login = student.Login)
LEFT JOIN teacher ON (User.Login = teacher.Login)
WHERE User.Login == '{user}';''', conn)


def get_profile(conn, user):
    return pd.read_sql(f''' SELECT Profile
        from User
        WHERE User.Login == '{user}';''', conn)
