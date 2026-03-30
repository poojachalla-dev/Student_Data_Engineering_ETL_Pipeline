import pandas as pd
import logging
from db_connection import get_connection


def extract_data():
    """
    Extract data from students, scores, and attendance tables.
    """
    conn = None
    try:
        conn = get_connection()
        logging.info("📥 Extracting data from database...")

        students = pd.read_sql("SELECT * FROM students", conn)
        scores = pd.read_sql("SELECT * FROM scores", conn)
        attendance = pd.read_sql("SELECT * FROM attendance", conn)

        # ✅ Validation: check empty tables
        if students.empty:
            raise ValueError("students table is empty")
        if scores.empty:
            raise ValueError("scores table is empty")
        if attendance.empty:
            raise ValueError("attendance table is empty")

        # ✅ Logging row counts (VERY important in real pipelines)
        logging.info(
            f"✅ Extracted rows → students: {len(students)}, "
            f"scores: {len(scores)}, attendance: {len(attendance)}"
        )

        return students, scores, attendance

    except Exception as e:
        logging.error(f"❌ Error during extraction: {e}")
        raise

    finally:
        if conn:
            conn.close()
