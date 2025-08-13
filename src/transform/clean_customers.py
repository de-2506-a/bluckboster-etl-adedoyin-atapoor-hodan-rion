import pandas as pd


def clean_customers(customers: pd.DataFrame) -> pd.DataFrame:
    # Handle Missing Values
    customers = remove_missing_values(customers)

    # Save the dataframe as a CSV for logging purposes
    # Ensure the directory exists
    customers.to_csv("data/processed/cleaned-customers.csv", index=False)
    return customers


def remove_missing_values(customers: pd.DataFrame) -> pd.DataFrame:
    # Remove unused columns and columns with missing values
    customers = customers.dropna(subset="address_id")

    return customers
