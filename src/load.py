def load_data(df):
    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            """INSERT INTO performance_summary 
            (student_id, name, average_marks, attendance_percentage, performance)
            VALUES (%s, %s, %s, %s, %s)""",
            (
                row['student_id'],
                row['name'],
                row['average_marks'],
                row['attendance_percentage'],
                row['performance']
            )
        )

    conn.commit()
    conn.close()
