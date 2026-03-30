import pandas as pd
import logging

def transform_data(students, scores, attendance, total_days=180):
    """
    Merge datasets, compute metrics, and generate multiple analytical datasets.
    """
    try:
        logging.info("🔄 Transforming data...")

        # ------------------ MERGE ------------------ #
        df = (
            students
            .merge(scores, on="student_id", how="inner")
            .merge(attendance, on="student_id", how="inner")
        )

        # ------------------ CLEANING ------------------ #
        df = df.drop_duplicates()

        df[['G1', 'G2', 'G3']] = df[['G1', 'G2', 'G3']].fillna(0)
        df['absences'] = df['absences'].fillna(0)

        # ------------------ METRICS ------------------ #
        df['average_marks'] = df[['G1', 'G2', 'G3']].mean(axis=1)

        df['attendance_percentage'] = (
            (total_days - df['absences']) / total_days
        ) * 100

        df['performance'] = pd.cut(
            df['average_marks'],
            bins=[0, 75, 90, 100],
            labels=["Needs Improvement", "Good", "Excellent"]
        )

        # ------------------ NEW FEATURES ------------------ #

        # 🎯 Improvement (progress tracking)
        df['improvement'] = df['G3'] - df['G1']

        # 🎯 Attendance bucket
        df['attendance_bucket'] = pd.cut(
            df['attendance_percentage'],
            bins=[0, 50, 75, 100],
            labels=['Low', 'Medium', 'High']
        )

        # ------------------ VIZ TABLES ------------------ #

        # 📊 1. Performance distribution
        performance_dist = (
            df['performance']
            .value_counts()
            .reset_index()
        )
        performance_dist.columns = ['performance', 'count']

        # 📊 2. Attendance distribution
        attendance_dist = (
            df['attendance_bucket']
            .value_counts()
            .reset_index()
        )
        attendance_dist.columns = ['attendance_bucket', 'count']

        # 📊 3. Top students
        top_students = (
            df[['student_id', 'average_marks']]
            .sort_values(by='average_marks', ascending=False)
            .head(10)
        )

        # 📊 4. Improvement distribution
        improvement_dist = (
            df['improvement']
            .describe()
            .reset_index()
        )
        improvement_dist.columns = ['metric', 'value']

        # 📊 5. Correlation matrix (for heatmap)
        correlation = df[['G1', 'G2', 'G3', 'absences']].corr().reset_index()

        # ------------------ FINAL CHECK ------------------ #
        if df.empty:
            raise ValueError("Transformed dataset is empty!")

        logging.info("✅ Transformation complete with multiple datasets")

        return (
            df,
            performance_dist,
            attendance_dist,
            top_students,
            improvement_dist,
            correlation
        )

    except Exception as e:
        logging.error(f"❌ Error during transformation: {e}")
        raise
