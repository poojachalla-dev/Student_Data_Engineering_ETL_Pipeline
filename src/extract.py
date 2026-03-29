import pandas as pd
import logging
from db_connection import get_connection

# ---------------------- EXTRACT ---------------------- #
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

        logging.info("✅ Data extraction successful")
        return students, scores, attendance

    except Exception as e:
        logging.error(f"❌ Error during extraction: {e}")
        raise

    finally:
        if conn:
            conn.close()
