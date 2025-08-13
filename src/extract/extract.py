import pandas as pd
from src.extract.extract_films import extract_films
from src.extract.extract_actors import extract_actors
from src.extract.extract_payments import extract_payments
from src.utils.logging_utils import setup_logger

logger = setup_logger("extract_data", "extract_data.log")


def extract_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    try:
        logger.info("Starting data extraction process")

        films = extract_films()
        actors = extract_actors()
        payments = extract_payments()

        logger.info(
            f"Data extraction completed successfully - "
            f"Films: {films.shape}, Actors: {actors.shape}"
        )

        return (films, actors, payments)

    except Exception as e:
        logger.error(f"Data extraction failed: {str(e)}")
        raise
