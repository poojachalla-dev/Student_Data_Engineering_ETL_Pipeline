import pandas as pd
from db_connection import get_connection

def transform_data(students, scores, attendance):
    """
    Merge students, scores, and attendance tables,
    calculate average marks and attendance percentage,
    assign performance category.
    """

    # Merge tables
    df = (
        students
        .merge(scores, on="student_id")
        .merge(attendance, on="student_id")
    )

    # Average marks from scores
    df['average_marks'] = df[['G1', 'G2', 'G3']].mean(axis=1)

    # Calculate attendance percentage
    TOTAL_DAYS = 180  # adjust if different
    df['attendance_percentage'] = ((TOTAL_DAYS - df['absences']) / TOTAL_DAYS) * 100

    # Performance category based on average marks
    def performance(avg):
        if avg >= 90:
            return "Excellent"
        elif avg >= 75:
            return "Good"
        else:
            return "Needs Improvement"

    df['performance'] = df['average_marks'].apply(performance)

    return df



def load_data(df):
    """
    Load transformed data into performance_summary table.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # 🧹 Step 1: Clear existing data (VERY IMPORTANT)
    cursor.execute("DELETE FROM performance_summary")

    # 💾 Step 2: Insert fresh data
    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO performance_summary 
            (student_id, average_marks, attendance_percentage, performance)
            VALUES (%s, %s, %s, %s)
            """,
            (
                row['student_id'],
                row['average_marks'],
                row['attendance_percentage'],
                row['performance']
            )
        )

    conn.commit()
    conn.close()


def extract_data():
    """
    Extract data from students, scores, and attendance tables.
    """
    conn = get_connection()

    students = pd.read_sql("SELECT * FROM students", conn)
    scores = pd.read_sql("SELECT * FROM scores", conn)
    attendance = pd.read_sql("SELECT * FROM attendance", conn)

    conn.close()

    return students, scores, attendance
