"""
Purpose :
    Load, clean, validate, and prepare the dataset for exploratory data analysis, statistical testing,
    machine learning modelling, and dashboard development.
"""

import pandas as pd

# Load data
def load_data(filepath):
    """Loads the raw dataset(CSV file).

    Parameters:
        filepath : str

    Returns:
        pd.DataFrame
    """
    return pd.read_csv(filepath, encoding='latin1')


def clean_data(df):

    """
    Clean and standardise dataset.

    Parameters:
        df : pd.DataFrame

    Returns:
        pd.DataFrame
    """
    # 1. Standardize headers: lower cases, replace spaces & hyphens with underscores, and strip white spaces
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_').str.strip()


    # 2. Convert date strings to datetime objects
    df["order_date"] = pd.to_datetime(df["order_date"], errors='coerce')
    df["ship_date"] = pd.to_datetime(df["ship_date"], errors='coerce')


    # 3. Calculate shipping duration in days for dashboard KPIs
    df["days_to_ship"] = (df["ship_date"] - df["order_date"]).dt.days


    # 4. Remove duplicate records
    before_rows = len(df)
    df = df.drop_duplicates()
    after_rows = len(df)
    print(f"Removed {before_rows - after_rows} duplicate rows.")


    # 5. Handle missing text values (Fill before converting to str to avoid "nan" strings)
    df["postal_code"] = df["postal_code"].fillna("Unknown")


    # 6. Strip whitespace from all text/string data rows
    string_cols = df.select_dtypes(include=['object']).columns
    for col in string_cols:
        df[col] = df[col].astype(str).str.strip()


    # 7. Numeric Type enforcement
    numeric_cols = ["sales", "profit", "quantity", "discount"]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df

def validate_data(df):
    """
    Perform data-quality checks.
    """

    print("\n////////////////////////")
    print("Missing values")
    print(df.isna().sum())

    print("\n////////////////////////")
    print("Negative shipping times")
    negative_shipping = df[df["days_to_ship"] < 0]  
    print(f"Negative shipping records: {len(negative_shipping)}")

    print("\n////////////////////////")
    print("Summary Ststistics")
    print(df[["sales", "profit", "quantity", "discount", "days_to_ship"]].describe())

if __name__ == "__main__":
    FILE_PATH = ("data/superstore.csv")

    df = load_data(FILE_PATH)

    df = clean_data(df)

    validate_data(df)

    print("\nDataset is ready for analysis.")

