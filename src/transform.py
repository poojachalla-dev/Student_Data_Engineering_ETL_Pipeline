import pandas as pd
import logging
from db_connection import get_connection

# ✅ Logging setup (industry standard)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------------- TRANSFORM ---------------------- #
def transform_data(students, scores, attendance, total_days=180):
    """
    Merge datasets, compute metrics, and assign performance categories.
    """
    try:
        logging.info("🔄 Transforming data...")

        # Merge datasets
        df = (
            students
            .merge(scores, on="student_id")
            .merge(attendance, on="student_id")
        )

        # Average marks (vectorized)
        df['average_marks'] = df[['G1', 'G2', 'G3']].mean(axis=1)

        # Attendance percentage
        df['attendance_percentage'] = (
            (total_days - df['absences']) / total_days
        ) * 100

        # Performance category (vectorized - faster than apply)
        df['performance'] = pd.cut(
            df['average_marks'],
            bins=[0, 75, 90, 100],
            labels=["Needs Improvement", "Good", "Excellent"]
        )

        logging.info("✅ Transformation complete")
        return df

    except Exception as e:
        logging.error(f"❌ Error during transformation: {e}")
        raise
