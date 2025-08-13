import pandas as pd
from typing import Tuple
from src.transform.clean_address import clean_address
from src.transform.clean_customers import clean_customers


def transform_data(data) -> Tuple[pd.DataFrame, pd.DataFrame]:
    cleaned_address = clean_address(data[5])
    cleaned_customers = clean_customers(data[2])

    return (cleaned_address, cleaned_customers)
