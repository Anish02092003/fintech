import csv
from typing import Dict

def parse_financial_csv(file) -> Dict:
    reader = csv.DictReader(
        (line.decode("utf-8") for line in file)
    )

    row = next(reader)

    return {
        "revenue": float(row["revenue"]),
        "net_profit": float(row["net_profit"]),
        "operating_profit": float(row.get("operating_profit", 0)),
        "total_assets": float(row["total_assets"]),
        "total_liabilities": float(row["total_liabilities"]),
        "total_debt": float(row["total_debt"]),
        "current_assets": float(row["current_assets"]),
        "current_liabilities": float(row["current_liabilities"]),
    }