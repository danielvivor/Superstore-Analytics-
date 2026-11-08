import os
import pandas as pd
from data_processing import load_data, clean_data

# Safely calculate the path relative to script's location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Move up one level out of 'src' into 'data'
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "superstore.csv")

# Load data using the file path string
raw_df = load_data(DATA_PATH)

# Clean raw data
df = clean_data(raw_df)


def loss_making_orders(df):
    return df[df["profit"] < 0]

def analyze_discount_bands(df):
    """
    Group orders into discount bands and calculate
    sales/profit metrics for each band.
    """

    discount_bins = [-0.01, 0.0, 0.20, 0.50, 0.81]

    labels = [
        "No Discount (0%)",
        "Low Discount (1%-20%)",
        "High Discount (21%-50%)",
        "Deep Discount (51%-80%)"
    ]

    df_copy = df.copy()

    df_copy["discount_band"] = pd.cut(
        df_copy["discount"],
        bins=discount_bins,
        labels=labels
    )

    return (
        df_copy.groupby("discount_band", observed=False)
        .agg(
            total_sales=("sales", "sum"),
            average_sales=("sales", "mean"),
            total_profit=("profit", "sum"),
            average_profit=("profit", "mean"),
            order_count=("order_id", "nunique")
        )
        .reset_index()
    )

def find_profitability_threshold(df):
    """
    Identify the lowest discount rate where
    aggregate profit becomes negative.
    """

    summary = (
        df.groupby("discount")["profit"]
        .sum()
        .reset_index()
    )

    loss_thresholds = summary.loc[
        summary["profit"] < 0,
        "discount"
    ]

    if not loss_thresholds.empty:
        return loss_thresholds.min()

    return None

def high_discount_losses(df, discount_threshold=0.20):
    """
    Find products that are both heavily discounted
    and generating negative profit.
    """

    losses = df[
        (df["discount"] >= discount_threshold) &
        (df["profit"] < 0)
    ]

    return (
        losses.groupby(
            ["category", "sub_category", "product_name"]
        )
        .agg(
            total_loss=("profit", "sum"),
            total_sales=("sales", "sum"),
            avg_discount=("discount", "mean")
        )
        .sort_values(
            by="total_loss",
            ascending=True
        )
        .reset_index()
    )

