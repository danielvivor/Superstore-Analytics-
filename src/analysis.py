"""
Purpose:
    Provides reusable analysis functions for 
    - Profitability, 
    - Discount,
    - Operational,
    - Customer Segment and 
    - Statistical Analysis
"""

import os
import pandas as pd

from data_processing import load_data, clean_data

# Load dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    BASE_DIR, "..", "data", "superstore.csv"
)

raw_df = load_data(DATA_PATH)
df = clean_data(raw_df)

# ................................
# Profitability Analysis
# ................................
def loss_making_orders(df):

    """
    Return all orders with negative profit.
    """
    return df[df["profit"] < 0]


def loss_making_products(df, top_n = 100):
    """
    Identify products generating the biggest losses.
    """

    return (
        df.groupby(["category", "sub_category", "product_name"]).agg(
            total_sales = ("sales", "sum"),
            total_loss = ("profit", "sum")
        ).sort_values(by="total_loss" ).head(top_n).reset_index()
    )

def profit_making_products(df, top_n = 100):
    """
    Identify products generating the biggest profits.
    """

    return (
        df.groupby(["category", "sub_category", "product_name"]).agg(
            total_sales = ("sales", "sum"),
            total_profit = ("profit", "sum")
        ).sort_values(by= "total_profit", ascending=False).head(top_n).reset_index()
    )

# ....................................
# Discount Analysis
# ....................................
def inspect_discount_intervals(df, col="discount", print_output=True):
    """
    Inspect unique discount values, summary statistics, and value counts.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing the discount column.
    col : str, default "discount"
        Name of the discount column.
    print_output : bool, default True
        Whether to print the summary to stdout.

    Returns
    -------
    dict
        Dictionary containing 'unique_values', 'summary_stats', and 'value_counts'.
    """
    series = df[col].dropna()
    unique_values = sorted(series.unique())
    summary_stats = series.describe()
    value_counts = series.value_counts().sort_index()

    if print_output:
        print("Unique sorted discounts:", unique_values)
        print("\nSummary statistics:")
        print(summary_stats)
        print("\nValue counts (sorted by discount):")
        print(value_counts)

    return {
        "unique_values": unique_values,
        "summary_stats": summary_stats,
        "value_counts": value_counts,
    }
