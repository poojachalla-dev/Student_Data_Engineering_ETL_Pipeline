from transform import extract_data, transform_data, load_data

def run_pipeline():
    students, scores, attendance = extract_data()
    transformed_df = transform_data(students, scores, attendance)
    load_data(transformed_df)

    print("Pipeline executed successfully!")

if __name__ == "__main__":
    run_pipeline()
