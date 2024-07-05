import pandas as pd

def list_teacher(conn):
    return pd.read_sql(
        f''' ''', conn
    )