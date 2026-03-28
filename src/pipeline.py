import logging
from extract import extract_data
from transform import transform_data
from load import load_data


# ✅ Logging setup (industry standard)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    logging.info("🚀 Pipeline started")

    students, scores, attendance = extract_data()
    logging.info("✅ Data extracted")

    transformed_df = transform_data(students, scores, attendance)
    logging.info("✅ Data transformed")

    load_data(transformed_df)
    logging.info("✅ Data loaded into database")

    logging.info("🎉 Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
