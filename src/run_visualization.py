from visualization import (
    load_all_data,
    plot_average_marks,
    plot_performance_counts,
    plot_attendance_distribution,
    plot_top_students,
    plot_improvement_stats,
    plot_correlation_heatmap
)

# Load all datasets
(
    df,
    performance_dist,
    attendance_dist,
    top_students,
    improvement_stats,
    correlation_matrix
) = load_all_data()

# -----------------------------
# Basic charts
# -----------------------------
plot_average_marks(df)
plot_performance_counts(performance_dist)

# -----------------------------
# More insights
# -----------------------------
plot_attendance_distribution(attendance_dist)
plot_top_students(top_students)
plot_improvement_stats(improvement_stats)

# -----------------------------
# Advanced analytics
# -----------------------------
plot_correlation_heatmap(correlation_matrix)
