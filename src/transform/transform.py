import pandas as pd
from typing import Tuple
from src.transform.clean_address import clean_address
from src.transform.clean_customers import clean_customers
from src.transform.clean_rental import clean_rental


def transform_data(data) -> Tuple[pd.DataFrame, pd.DataFrame]:
    cleaned_address = clean_address(data[5])
    cleaned_customers = clean_customers(data[2])
    cleaned_rental = clean_rental(data[3])
    
    return (cleaned_address, cleaned_customers, cleaned_rental)