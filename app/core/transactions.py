import pandas as pd


def parse_transactions_csv(file_path: str):
    df = pd.read_csv(file_path)

    required_cols = {"date", "amount", "type"}
    if not required_cols.issubset(df.columns):
        raise ValueError("CSV must contain date, amount, and type columns")

    # Ensure correct types
    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = df["amount"].astype(float)

    # Only consider debit (expenses)
    df = df[df["type"].str.lower() == "debit"]

    return df


def aggregate_monthly_spending(df):
    df["month"] = df["date"].dt.to_period("M")

    monthly_spend = df.groupby("month")["amount"].sum().abs()

    mean_spend = monthly_spend.mean()
    std_spend = monthly_spend.std()

    return {
        "monthly_spend_mean": round(mean_spend, 2),
        "monthly_spend_std": round(std_spend if not pd.isna(std_spend) else 0, 2)
    }