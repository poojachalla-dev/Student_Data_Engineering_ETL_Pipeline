import matplotlib.pyplot as plt
import pandas as pd
from db_connection import get_connection

def load_data_for_visualization():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM performance_summary", conn)
    conn.close()
    return df

def plot_average_marks(df):
    plt.figure()
    plt.hist(df['average_marks'])
    plt.title("Average Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.show()

def plot_performance_counts(df):
    counts = df['performance'].value_counts()

    plt.figure()
    counts.plot(kind='bar')
    plt.title("Performance Categories")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.show()
