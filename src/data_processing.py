import pandas as pd

# Load data
def load_data(filepath):
    """Loads the raw Superstore CSV file safely using Latin1 encoding."""
    return pd.read_csv(filepath, encoding='latin1')

def clean_data(df):

    """
    Clean and standardise the Superstore dataset.

    Parameters:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame
    """
    # 1. Standardize headers: lowercase, replace spaces & hyphens with underscores, and strip margins
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_').str.strip()


    # 2. Convert date strings to datetime objects
    df["order_date"] = pd.to_datetime(df["order_date"], errors='coerce')
    df["ship_date"] = pd.to_datetime(df["ship_date"], errors='coerce')


    # 3. Calculate shipping duration in days for dashboard KPIs
    df["days_to_ship"] = (df["ship_date"] - df["order_date"]).dt.days


    # 4. Drop exact duplicate rows
    df = df.drop_duplicates()


    # 5. Handle missing text values (Fill before converting to str to avoid "nan" strings)
    df["postal_code"] = df["postal_code"].fillna("Unknown")


    # 6. Strip whitespace from all text/string data rows
    string_cols = df.select_dtypes(include=['object']).columns
    for col in string_cols:
        df[col] = df[col].astype(str).str.strip()


    # 7. Ensure numerical columns are strictly treated as numbers
    numeric_cols = ["sales", "profit", "quantity", "discount"]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df
    