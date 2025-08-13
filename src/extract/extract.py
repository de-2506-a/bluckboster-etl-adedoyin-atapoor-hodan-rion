import pandas as pd
from src.extract.extract_films import extract_films
from src.extract.extract_payments import extract_payments
from src.extract.extract_customers import extract_customers
from src.extract.extract_rental import extract_rental
from src.extract.extract_city import extract_city
from src.extract.extract_address import extract_address
from src.extract.extract_inventory import extract_inventory
from src.extract.extract_country import extract_country
from src.utils.logging_utils import setup_logger

logger = setup_logger("extract_data", "extract_data.log")


def extract_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    try:
        logger.info("Starting data extraction process")

        films = extract_films()
        payments = extract_payments()
        customers = extract_customers()
        rental = extract_rental()
        city = extract_city()
        address = extract_address()
        inventory = extract_inventory()
        country = extract_country()

        logger.info(
            f"Data extraction completed successfully - "
            f"Films: {films.shape}, "
            f"Payments: {payments.shape}, "
            f"Customers: {customers.shape}, "
            f"Rentals: {rental.shape}, "
            f"City: {city.shape}, "
            f"Address: {address.shape}, "
            f"Inventory: {inventory.shape}, "
            f"Country: {country.shape}"
        )

        return (films, payments, customers, rental, city, address, inventory,
                country)

    except Exception as e:
        logger.error(f"Data extraction failed: {str(e)}")
        raise
