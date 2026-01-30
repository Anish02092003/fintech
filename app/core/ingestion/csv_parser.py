import csv
from io import StringIO
from typing import List
from app.api.schemas.company_csv import CompanyYearData


REQUIRED_COLUMNS = {
    "year", "revenue", "net_profit", "total_assets",
    "total_liabilities", "total_equity",
    "current_assets", "current_liabilities", "total_debt"
}


def parse_company_csv(content: str) -> List[CompanyYearData]:
    reader = csv.DictReader(StringIO(content))

    if not REQUIRED_COLUMNS.issubset(reader.fieldnames):
        missing = REQUIRED_COLUMNS - set(reader.fieldnames)
        raise ValueError(f"Missing columns: {missing}")

    records = []
    for row in reader:
        records.append(CompanyYearData(**row))

    if len(records) < 2:
        raise ValueError("At least 2 years of data required")

    return records