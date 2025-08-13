import pandas as pd


def clean_rental(rental: pd.DataFrame) -> pd.DataFrame:
    # Task 2 - Remove rows with missing values
    rental = remove_missing_values(rental)
    
    # Save the dataframe as a CSV for logging purposes
    rental.to_csv("data/processed/cleaned-rental.csv", index=False)
    return rental


def remove_missing_values(rental: pd.DataFrame) -> pd.DataFrame:
    rental = rental.dropna(subset=["return_date"])

    return rental