import pandas as pd
from db_connection import get_connection
import os

# Get project root (go one level up from src)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_csv(filename):
    file_path = os.path.join(DATA_DIR, filename)
    print(f"📂 Loading: {file_path}")
    return pd.read_csv(file_path)


def insert_students(cursor, df):
    query = """
        INSERT INTO students (
            student_id, school, sex, age, address,
            famsize, Pstatus, Medu, Fedu, Mjob, Fjob
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = list(df.itertuples(index=False, name=None))
    cursor.executemany(query, data)
    print("✅ Students inserted")


def insert_scores(cursor, df):
    query = """
        INSERT INTO scores (student_id, G1, G2, G3)
        VALUES (%s, %s, %s, %s)
    """
    data = list(df.itertuples(index=False, name=None))
    cursor.executemany(query, data)
    print("✅ Scores inserted")


def insert_attendance(cursor, df):
    query = """
        INSERT INTO attendance (student_id, absences)
        VALUES (%s, %s)
    """
    data = list(df.itertuples(index=False, name=None))
    cursor.executemany(query, data)
    print("✅ Attendance inserted")


def run_pipeline():
    conn = None
    try:
        # 🔹 Load all CSVs
        students_df = load_csv("students.csv")
        scores_df = load_csv("scores.csv")
        attendance_df = load_csv("attendance.csv")

        # 🔹 Connect to DB
        conn = get_connection()
        cursor = conn.cursor()

        # 🔹 Insert in correct order (VERY IMPORTANT)
        insert_students(cursor, students_df)
        insert_scores(cursor, scores_df)
        insert_attendance(cursor, attendance_df)

        conn.commit()
        print("🚀 Data ingestion completed successfully!")

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"❌ Pipeline failed: {e}")

    finally:
        if conn:
            conn.close()
            print("🔒 Connection closed")


if __name__ == "__main__":
    run_pipeline()
