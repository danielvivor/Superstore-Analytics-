"""
analysis.py

Reusable business-analysis functions. Provides functionality for:

- Profitability Analysis
- Discount Analysis
- Operational Analysis
- Correlation Analysis
- Customer Segmentation preparation
"""

import pandas as pd

# .....................................
# Profitability Analysis
# .....................................

def loss_making_orders(df):
    """
    Return all orders with negative profit.
    """
    return df[df["profit"] < 0]


def top_loss_making_products(df, top_n=100):
    """
    Identify products generating the biggest losses.
    """

    return (
        df.groupby(
            ["category", "sub_category", "product_name"]
        )
        .agg(
            total_sales=("sales", "sum"),
            total_loss=("profit", "sum")
        )
        .sort_values(
            by="total_loss",
            ascending=True
        )
        .head(top_n)
        .reset_index()
    )


def top_profit_making_products(df, top_n=100):
    """
    Identify products generating the biggest profits.
    """

    return (
        df.groupby(
            ["category", "sub_category", "product_name"]
        )
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum")
        )
        .sort_values(
            by="total_profit",
            ascending=False
        )
        .head(top_n)
        .reset_index()
    )


# ...............................
# Discount Analysis
# ...............................

def inspect_discount_intervals(
    df,
    column="discount",
    print_output=True
):
    """
    Inspect available discount values and distributions.
    """

    series = df[column].dropna()

    results = {
        "unique_values": sorted(series.unique()),
        "summary_stats": series.describe(),
        "value_counts": series.value_counts().sort_index()
    }

    if print_output:
        print("Unique Discounts:")
        print(results["unique_values"])

        print("\nSummary Statistics:")
        print(results["summary_stats"])

        print("\nDiscount Counts:")
        print(results["value_counts"])

    return results


def analyze_discount_bands(df):
    """
    Create business-friendly discount tiers and
    summarise profitability by discount level.
    """

    bins = [
        -0.001,
        0.00,
        0.20,
        0.32,
        0.50,
        1.00
    ]

    labels = [
        "0% (No Discount)",
        "1-20% (Low)",
        "21-32% (Moderate)",
        "33-50% (High)",
        ">50% (Aggressive)"
    ]

    temp = df.copy()

    temp["discount_band"] = pd.cut(
        temp["discount"],
        bins=bins,
        labels=labels
    )

    return (
        temp.groupby(
            "discount_band",
            observed=False
        )
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
    Find the lowest discount level where
    cumulative profit becomes negative.
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


def high_discount_losses(
    df,
    discount_threshold=0.30
):
    """
    Identify products receiving high discounts
    while generating losses.
    """

    losses = df[
        (df["discount"] >= discount_threshold)
        &
        (df["profit"] < 0)
    ]

    return (
        losses.groupby(
            [
                "category",
                "sub_category",
                "product_name"
            ]
        )
        .agg(
            total_loss=("profit", "sum"),
            total_sales=("sales", "sum"),
            avg_discount=("discount", "mean")
        )
        .sort_values(
            by="total_loss"
        )
        .reset_index()
    )


# ..........................
# Opertional Analysis
# ..........................

def shipping_performance(df):
    """
    Shipping duration summary statistics.
    """

    return {
        "average_days_to_ship":
            round(df["days_to_ship"].mean(), 2),

        "maximum_days_to_ship":
            df["days_to_ship"].max(),

        "minimum_days_to_ship":
            df["days_to_ship"].min()
    }


# ..............................
# Descriptive Statistics
# ..............................

def descriptive_statistics(df):
    """
    Numerical summary statistics.
    """

    numeric_cols = [
        "sales",
        "profit",
        "quantity",
        "discount",
        "days_to_ship"
    ]

    return df[numeric_cols].describe()


# .......................
# Correlation Analysis
# .......................

def correlation_matrix(
    df,
    method="pearson"
):
    """
    Generate a correlation matrix.

    Parameters
    ----------
    method : str
        'pearson' or 'spearman'
    """

    numeric_cols = [
        "sales",
        "profit",
        "quantity",
        "discount",
        "days_to_ship"
    ]

    return (
        df[numeric_cols]
        .corr(method=method)
        .round(3)
    )


# ................................
# Statistical testing preparation
# ................................

def regional_profit_groups(df):
    """
    Return profit grouped by region.

    Useful for:
    - ANOVA
    - Kruskal-Wallis
    """

    return {
        region: group["profit"]
        for region, group
        in df.groupby("region")
    }


# .....................................
# Customer Segment preparation
# .....................................

def customer_metrics(df):
    """
    Aggregate customer-level metrics.

    Useful for:
    - K-Means Clustering
    - Customer Segmentation
    """

    return (
        df.groupby("customer_id")
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            order_count=("order_id", "nunique"),
            total_quantity=("quantity", "sum")
        )
        .reset_index()
    )