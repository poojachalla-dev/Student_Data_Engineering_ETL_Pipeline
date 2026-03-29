import logging
from extract import extract_data
from transform import transform_data
from load import load_data


# ✅ Logging setup (industry standard)
logging.basicConfig(
    filename="pipeline.log",   # 👈 log file name
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    logging.info("🚀 Pipeline started")

    try:
        students, scores, attendance = extract_data()
        logging.info("✅ Data extracted")
    except Exception as e:
        logging.error("❌ Extraction failed", exc_info=True)
        raise

    try:
        transformed_df = transform_data(students, scores, attendance)
        logging.info("✅ Data transformed")
    except Exception as e:
        logging.error("❌ Transformation failed", exc_info=True)
        raise

    try:
        load_data(transformed_df)
        logging.info("✅ Data loaded into database")
    except Exception as e:
        logging.error("❌ Load failed", exc_info=True)
        raise

    logging.info("🎉 Pipeline completed successfully")


if __name__ == "__main__":
        run_pipeline()
  