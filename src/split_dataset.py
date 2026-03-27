import pandas as pd

# Load dataset
df = pd.read_csv("../data/kaggle_dataset_students.csv")

# Add student_id (VERY IMPORTANT for database)
df["student_id"] = range(1, len(df) + 1)

# -------------------------
# 1. Students Table
# -------------------------
students = df[[
    "student_id",
    "school", "sex", "age", "address",
    "famsize", "Pstatus", "Medu", "Fedu",
    "Mjob", "Fjob"
]]

# -------------------------
# 2. Scores Table
# -------------------------
scores = df[[
    "student_id",
    "G1", "G2", "G3"
]]

# -------------------------
# 3. Attendance Table
# -------------------------
attendance = df[[
    "student_id",
    "absences"
]]

# Save files
students.to_csv("../data/students.csv", index=False)
scores.to_csv("../data/scores.csv", index=False)
attendance.to_csv("../data/attendance.csv", index=False)

print("✅ Data split into 3 files successfully!")
