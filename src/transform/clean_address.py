import pandas as pd


def clean_address(address: pd.DataFrame) -> pd.DataFrame:
    # Handle Missing Values
    address = remove_missing_values(address)

    # Save the dataframe as a CSV for logging purposes
    # Ensure the directory exists
    address.to_csv("data/processed/cleaned-address.csv", index=False)
    return address


def remove_missing_values(address: pd.DataFrame) -> pd.DataFrame:
    # Remove unused columns and columns with missing values
    address.drop(
        ["address2", "district", "phone", "last_update", "postal_code"],
        axis=1,
        inplace=True
    )

    return address
