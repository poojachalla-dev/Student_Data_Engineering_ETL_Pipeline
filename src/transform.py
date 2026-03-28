def transform_data(students, scores, attendance):

    # Merge all tables
    df = students.merge(scores, on="student_id") \
                 .merge(attendance, on="student_id")

    # Calculate average marks
    df['average_marks'] = df[['math', 'science', 'english']].mean(axis=1)

    # Performance category
    def performance(avg):
        if avg >= 90:
            return "Excellent"
        elif avg >= 75:
            return "Good"
        else:
            return "Needs Improvement"

    df['performance'] = df['average_marks'].apply(performance)

    return df
