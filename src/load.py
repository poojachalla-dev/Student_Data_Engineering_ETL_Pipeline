import pandas as pd
import logging
from db_connection import get_connection

# ✅ Logging setup (industry standard)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------------- LOAD ---------------------- #
def load_data(df):
    """
    Load transformed data into performance_summary table.
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        logging.info("🧹 Clearing old data...")
        cursor.execute("TRUNCATE TABLE performance_summary")

        logging.info("💾 Loading new data...")

        # Prepare batch data (faster than row-by-row inserts)
        data = list(zip(
            df['student_id'],
            df['average_marks'],
            df['attendance_percentage'],
            df['performance']
        ))

        cursor.executemany(
            """
            INSERT INTO performance_summary 
            (student_id, average_marks, attendance_percentage, performance)
            VALUES (%s, %s, %s, %s)
            """,
            data
        )

        conn.commit()
        logging.info("✅ Data loaded successfully")

    except Exception as e:
        logging.error(f"❌ Error during loading: {e}")
        raise

    finally:
        if conn:
            conn.close()
