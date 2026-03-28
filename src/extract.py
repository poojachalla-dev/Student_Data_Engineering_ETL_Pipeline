import pandas as pd
from db_connection import get_connection

def extract_data():
    conn = get_connection()

    students = pd.read_sql("SELECT * FROM students", conn)
    scores = pd.read_sql("SELECT * FROM scores", conn)
    attendance = pd.read_sql("SELECT * FROM attendance", conn)

    conn.close()

    return students, scores, attendance
