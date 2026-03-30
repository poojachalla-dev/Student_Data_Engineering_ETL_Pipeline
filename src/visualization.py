import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from db_connection import get_connection


# -----------------------------
# 1️⃣ Load ALL tables from DB
# -----------------------------
def load_all_data():
    conn = get_connection()

    performance_summary = pd.read_sql("SELECT * FROM performance_summary", conn)
    performance_dist = pd.read_sql("SELECT * FROM performance_distribution", conn)
    attendance_dist = pd.read_sql("SELECT * FROM attendance_distribution", conn)
    top_students = pd.read_sql("SELECT * FROM top_students", conn)
    improvement_stats = pd.read_sql("SELECT * FROM improvement_stats", conn)
    correlation_matrix = pd.read_sql("SELECT * FROM correlation_matrix", conn)

    conn.close()

    return (
        performance_summary,
        performance_dist,
        attendance_dist,
        top_students,
        improvement_stats,
        correlation_matrix
    )


# -----------------------------
# 2️⃣ Basic Visualizations
# -----------------------------
def plot_average_marks(df):
    plt.figure(figsize=(8,5))
    plt.hist(df['average_marks'], bins=10, color='skyblue', edgecolor='black')
    plt.title("Average Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.show()


def plot_performance_counts(performance_dist):
    plt.figure(figsize=(8,5))
    plt.bar(performance_dist['performance'], performance_dist['count'], color='salmon')
    plt.title("Performance Distribution")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.show()


# -----------------------------
# 3️⃣ Attendance Distribution
# -----------------------------
def plot_attendance_distribution(attendance_dist):
    plt.figure(figsize=(8,5))
    plt.bar(attendance_dist['attendance_bucket'], attendance_dist['count'])
    plt.title("Attendance Distribution")
    plt.xlabel("Attendance Level")
    plt.ylabel("Number of Students")
    plt.show()


# -----------------------------
# 4️⃣ Top Students
# -----------------------------
def plot_top_students(top_students):
    plt.figure(figsize=(10,5))
    plt.bar(top_students['student_id'].astype(str), top_students['average_marks'])
    plt.title("Top 10 Students")
    plt.xlabel("Student ID")
    plt.ylabel("Average Marks")
    plt.xticks(rotation=45)
    plt.show()


# -----------------------------
# 5️⃣ Improvement Stats
# -----------------------------
def plot_improvement_stats(improvement_stats):
    plt.figure(figsize=(8,5))
    plt.bar(improvement_stats['metric'], improvement_stats['value'])
    plt.title("Improvement Statistics (G3 - G1)")
    plt.xticks(rotation=45)
    plt.show()


# -----------------------------
# 6️⃣ Correlation Heatmap
# -----------------------------
def plot_correlation_heatmap(correlation_matrix):
    plt.figure(figsize=(10,8))

    # Set index for proper heatmap format
    corr = correlation_matrix.set_index('feature')

    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()
