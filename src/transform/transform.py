import pandas as pd
from typing import Tuple
from src.transform.clean_address import clean_address


def transform_data(data) -> Tuple[pd.DataFrame, pd.DataFrame]:
    cleaned_address = clean_address(data[5])

    return (cleaned_address)
