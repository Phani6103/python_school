from __future__ import annotations

from pathlib import Path
from typing import Optional

import pandas as pd

from python_school.services import YFinanceService


class PdCoreConcepts:
    simple_dict = {
        "Id": [1, 2, 3],
        "Name": ['Apple', 'Banana', 'Carrot'],
        "Salary": [100, 200, 300]
    }
    simple_df = pd.DataFrame(simple_dict)

    def __init__(self, finance_service: Optional[YFinanceService] = None):
        print("Welcome to Pandas Core Concepts!!")
        self.finance_service = finance_service or YFinanceService()

    def export_csv(self):
        self.simple_df.to_csv("simple_df", index=False)

    def import_csv(self):
        df = pd.read_csv("simple_df")
        print(df)

    def read_csv(self, ticker: str = "TSLA", period: str = "1d", interval: str = "1m") -> pd.DataFrame:
        """
        Download real-time stock data for the given ticker and persist it to disk.

        Args:
            ticker: Symbol to request market data for. Defaults to Tesla (TSLA).
            period: Lookback window accepted by yfinance (e.g. "1d", "5d").
            interval: Sampling interval (e.g. "1m" for per-minute data).
        """
        frame = self.finance_service.fetch_ticker(ticker, period, interval)
        print(frame)
        return frame


if __name__=="__main__":
    my_class = PdCoreConcepts()
    print(my_class.simple_dict)
    print(my_class.simple_df)
    my_class.export_csv()
    my_class.import_csv()
    try:
        tsla_df = my_class.read_csv()
        print(tsla_df)
    except ValueError as exc:
        print(f"Unable to fetch TSLA data: {exc}")
