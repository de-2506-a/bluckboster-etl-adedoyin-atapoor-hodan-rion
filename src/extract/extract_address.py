import logging
import os
import pandas as pd
import timeit
from config.db_config import load_db_config
from src.extract.extract_query import execute_extract_query
from src.utils.sql_utils import import_sql_query
from src.utils.db_utils import get_db_connection
from src.utils.logging_utils import setup_logger, log_extract_success

# Setup the logger
logger = setup_logger(__name__, "extract_data.log", level=logging.DEBUG)

EXTRACT_ADDRESS_QUERY_FILE = os.path.join(
    os.path.dirname(__file__), "../sql/extract_address.sql"
)

EXPECTED_IMPORT_RATE = 0.001

TYPE = "ADDRESS from pagila database"


def extract_address() -> pd.DataFrame:
    try:
        # Performance recording
        start_time = timeit.default_timer()
        address = extract_address_execution()
        extract_address_execution_time = (
            timeit.default_timer() - start_time
        )
        log_extract_success(
            logger,
            TYPE,
            address.shape,
            extract_address_execution_time,
            EXPECTED_IMPORT_RATE,
        )
        return address
    except Exception as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Failed to extract data: {e}")
        raise Exception(f"Failed to extract data: {e}")


def extract_address_execution() -> pd.DataFrame:
    # Import the SQL query
    connection_details = load_db_config()["source_database"]
    print(connection_details)
    query = import_sql_query(EXTRACT_ADDRESS_QUERY_FILE)

    # Connect to the database
    connection = get_db_connection(connection_details)

    # Execute the query
    address_df = execute_extract_query(query, connection)
    connection.close()

    # Return the created DataFrame
    return address_df
