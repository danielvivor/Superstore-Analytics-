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

result = loss_making_products(df)
print(result)
