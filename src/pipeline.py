import logging
from extract import extract_data
from transform import transform_data
from load import load_data

# ✅ Logging setup (industry standard)
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    logging.info("🚀 Pipeline started")

    # ---------------------- EXTRACT ---------------------- #
    try:
        students, scores, attendance = extract_data()
        logging.info("✅ Data extracted")
    except Exception:
        logging.error("❌ Extraction failed", exc_info=True)
        raise

    # ---------------------- TRANSFORM ---------------------- #
    try:
        (
            df,
            perf_dist,
            att_dist,
            top_students,
            improvement_dist,
            correlation
        ) = transform_data(students, scores, attendance)

        logging.info("✅ Data transformed")
    except Exception:
        logging.error("❌ Transformation failed", exc_info=True)
        raise

    # ---------------------- LOAD ---------------------- #
    try:
        load_data(
            df,
            perf_dist,
            att_dist,
            top_students,
            improvement_dist,
            correlation
        )
        logging.info("✅ Data loaded into database")
    except Exception:
        logging.error("❌ Load failed", exc_info=True)
        raise

    logging.info("🎉 Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()
