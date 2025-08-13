import pandas as pd
from src.extract.extract_films import extract_films
from src.utils.logging_utils import setup_logger

logger = setup_logger("extract_data", "extract_data.log")


def extract_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    try:
        logger.info("Starting data extraction process")

        films = extract_films()

        logger.info(
            f"Data extraction completed successfully - "
            f"Films: {films.shape}"
        )

        return (films)

    except Exception as e:
        logger.error(f"Data extraction failed: {str(e)}")
        raise
