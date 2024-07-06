import pandas as pd


def list_teacher(conn):
    return pd.read_sql(
        f'''SELECT Id,
    CASE
        WHEN Name IS NOT NULL THEN Name
        ELSE Login
    END AS Name
FROM teacher; ''', conn)


def list_student(conn):
    return pd.read_sql(
        f'''SELECT Id,
    CASE
        WHEN Name IS NOT NULL THEN Name
        ELSE Login
    END AS Name
FROM student; ''', conn)
