# app/services/pdf_parser.py

import pdfplumber
from typing import Dict, List
from app.api.schemas.company import CompanyFinancials


# =====================================================
# CONFIG
# =====================================================

FINANCIAL_SECTION_KEYWORDS = [
    "statement of profit",
    "statement of loss",
    "profit and loss",
    "income statement",
    "balance sheet",
    "statement of financial position",
]

VALUE_KEYWORDS = {
    "revenue": ["revenue", "total income"],
    "net_profit": ["net profit", "profit for the year"],
    "operating_profit": ["operating profit"],
    "total_assets": ["total assets"],
    "total_liabilities": ["total liabilities"],
    "total_debt": ["borrowings", "total debt"],
    "current_assets": ["current assets"],
    "current_liabilities": ["current liabilities"],
}


# =====================================================
# PAGE DETECTION
# =====================================================

def detect_financial_pages(pdf) -> List[int]:
    """
    Detect likely financial statement pages.
    Hard cap to stay safe on 300+ page PDFs.
    """
    pages = []

    for i, page in enumerate(pdf.pages):
        text = (page.extract_text() or "").lower()
        if any(k in text for k in FINANCIAL_SECTION_KEYWORDS):
            pages.append(i)

        if i > 150:   # 🔒 safety cap
            break

    return pages


# =====================================================
# TEXT VALUE EXTRACTION (fallback)
# =====================================================

def extract_value(text: str, keywords: List[str]):
    for line in text.split("\n"):
        if any(k in line.lower() for k in keywords):
            tokens = line.replace(",", "").split()
            for t in tokens:
                try:
                    return float(t)
                except ValueError:
                    continue
    return None


# =====================================================
# TABLE EXTRACTION (CORE FOR ANNUAL REPORTS)
# =====================================================

def extract_tables_from_pages(pdf, pages: list) -> list:
    """
    Extract tables from selected pages only.
    """
    rows = []

    for p in pages:
        page = pdf.pages[p]
        tables = page.extract_tables(
            table_settings={
                "vertical_strategy": "lines",
                "horizontal_strategy": "lines",
                "intersection_tolerance": 5,
            }
        )

        for table in tables:
            rows.extend(table)

    return rows


def parse_financial_table_rows(rows: list) -> Dict:
    """
    Convert financial tables into structured values.
    Works for Infosys / TCS formats.
    """
    data = {}

    for row in rows:
        if not row or len(row) < 2:
            continue

        label = (row[0] or "").lower()
        value = row[-1]

        for field, keys in VALUE_KEYWORDS.items():
            if any(k in label for k in keys):
                try:
                    data[field] = float(
                        str(value)
                        .replace(",", "")
                        .replace("(", "-")
                        .replace(")", "")
                    )
                except Exception:
                    pass

    return data


# =====================================================
# MAIN PARSER
# =====================================================

def parse_financial_pdf(file, pdf_type: str = "summary") -> Dict:
    """
    pdf_type:
    - summary        → small PDFs
    - annual_report  → Infosys / TCS / 300+ pages
    """

    with pdfplumber.open(file) as pdf:

        # -------------------------------------------------
        # ANNUAL REPORT MODE (TABLE FIRST)
        # -------------------------------------------------
        if pdf_type == "annual_report":
            pages = detect_financial_pages(pdf)

            if not pages:
                raise ValueError("Financial statements not found")

            # 🔥 Extract tables from ONLY a few pages
            rows = extract_tables_from_pages(pdf, pages[:3])
            data = parse_financial_table_rows(rows)

            if data:
                return data

            # -------- fallback to text if tables fail --------
            extracted_text = ""
            for p in pages[:2]:
                extracted_text += pdf.pages[p].extract_text() or ""

        # -------------------------------------------------
        # SUMMARY MODE
        # -------------------------------------------------
        else:
            extracted_text = "\n".join(
                page.extract_text() or ""
                for page in pdf.pages[:10]
            )

        # -------------------------------------------------
        # TEXT EXTRACTION (COMMON)
        # -------------------------------------------------
        data = {}
        for field, keys in VALUE_KEYWORDS.items():
            data[field] = extract_value(extracted_text, keys)

            if all(v in (None, 0) for v in data.values()):
             raise ValueError("No financial data detected in PDF")

        return data


# =====================================================
# NORMALIZER → Pydantic Model
# =====================================================

def pdf_to_company_financials(
    pdf_data: Dict,
    company_name: str
) -> CompanyFinancials:

    def safe(v):
        return v if v is not None else 0

    total_assets = safe(pdf_data.get("total_assets"))
    total_liabilities = safe(pdf_data.get("total_liabilities"))

    return CompanyFinancials(
        company_name=company_name,
        revenue=safe(pdf_data.get("revenue")),
        net_profit=safe(pdf_data.get("net_profit")),
        operating_profit=safe(pdf_data.get("operating_profit")),
        total_assets=total_assets,
        total_liabilities=total_liabilities,
        total_debt=safe(pdf_data.get("total_debt")),
        current_assets=safe(pdf_data.get("current_assets")),
        current_liabilities=safe(pdf_data.get("current_liabilities")),
        total_equity=total_assets - total_liabilities,
    )