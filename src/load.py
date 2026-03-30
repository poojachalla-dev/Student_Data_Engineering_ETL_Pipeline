import logging
from db_connection import get_connection


def load_data(
    df,
    perf_dist,
    att_dist,
    top_students,
    improvement_dist,
    correlation
):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        logging.info("💾 Loading all datasets...")

        # ------------------ 1. MAIN TABLE ------------------ #
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS performance_summary (
            student_id INT PRIMARY KEY,
            average_marks FLOAT,
            attendance_percentage FLOAT,
            performance VARCHAR(50)
        )
        """)

        cursor.execute("TRUNCATE TABLE performance_summary")

        cursor.executemany(
            """
            INSERT INTO performance_summary
            (student_id, average_marks, attendance_percentage, performance)
            VALUES (%s, %s, %s, %s)
            """,
            list(zip(
                df['student_id'],
                df['average_marks'],
                df['attendance_percentage'],
                df['performance']
            ))
        )

        # ------------------ 2. PERFORMANCE DIST ------------------ #
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS performance_distribution (
            performance VARCHAR(50),
            count INT
        )
        """)

        cursor.execute("TRUNCATE TABLE performance_distribution")

        cursor.executemany(
            "INSERT INTO performance_distribution VALUES (%s, %s)",
            list(zip(perf_dist['performance'], perf_dist['count']))
        )

        # ------------------ 3. ATTENDANCE DIST ------------------ #
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance_distribution (
            attendance_bucket VARCHAR(50),
            count INT
        )
        """)

        cursor.execute("TRUNCATE TABLE attendance_distribution")

        cursor.executemany(
            "INSERT INTO attendance_distribution VALUES (%s, %s)",
            list(zip(att_dist['attendance_bucket'], att_dist['count']))
        )

        # ------------------ 4. TOP STUDENTS ------------------ #
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS top_students (
            student_id INT,
            average_marks FLOAT
        )
        """)

        cursor.execute("TRUNCATE TABLE top_students")

        cursor.executemany(
            "INSERT INTO top_students VALUES (%s, %s)",
            list(zip(
                top_students['student_id'],
                top_students['average_marks']
            ))
        )

        # ------------------ 5. IMPROVEMENT STATS ------------------ #
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS improvement_stats (
            metric VARCHAR(50),
            value FLOAT
        )
        """)

        cursor.execute("TRUNCATE TABLE improvement_stats")

        cursor.executemany(
            "INSERT INTO improvement_stats VALUES (%s, %s)",
            list(zip(
                improvement_dist['metric'],
                improvement_dist['value']
            ))
        )

        # ------------------ 6. CORRELATION ------------------ #
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS correlation_matrix (
            feature VARCHAR(50),
            G1 FLOAT,
            G2 FLOAT,
            G3 FLOAT,
            absences FLOAT
        )
        """)

        cursor.execute("TRUNCATE TABLE correlation_matrix")

        cursor.executemany(
            "INSERT INTO correlation_matrix VALUES (%s, %s, %s, %s, %s)",
            correlation.values.tolist()
        )

        # ------------------ COMMIT ------------------ #
        conn.commit()
        logging.info("✅ All datasets loaded successfully")

    except Exception as e:
        if conn:
            conn.rollback()
        logging.error(f"❌ Error during loading: {e}")
        raise

    finally:
        if conn:
            conn.close()
