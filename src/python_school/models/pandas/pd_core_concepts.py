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
    symbol = "TSLA"
    data_dir = Path("test_data")

    def __init__(self, finance_service: Optional[YFinanceService] = None):
        print("Welcome to Pandas Core Concepts!!")
        self.finance_service = finance_service or YFinanceService()

    def export_csv(self):
        self.simple_df.to_csv("simple_df", index=False)

    def import_csv(self) -> None:
        df = pd.read_csv("simple_df")
        print(df)

    def fetch_realtime_csv(self, ticker: str = "TSLA", period: str = "1d", interval: str = "1m") -> Path:
        """Download fresh stock data for the given ticker and write it to CSV."""
        frame = self.finance_service.fetch_ticker(ticker, period, interval)
        csv_path = self.finance_service.save_file(ticker, frame, directory=self.data_dir)
        print(f"Saved {ticker.upper()} data to {csv_path}")
        return csv_path

    def read_csv(self, ticker: str = "TSLA") -> pd.DataFrame:
        """Read cached CSV data for the requested ticker."""
        csv_path = self.data_dir / f"{ticker.upper()}.csv"
        if not csv_path.exists():
            raise FileNotFoundError(
                f"CSV for {ticker} not found at {csv_path}. "
                "Call fetch_realtime_csv first to download fresh data."
            )
        return pd.read_csv(csv_path, parse_dates=["Datetime"])

    def set_index(self) -> None:
        df = self.read_csv()
        print("Before: ", df)
        df.set_index("Datetime", inplace=True)
        print("After: ", df)

    def describe_data(self) -> None:
        df = self.read_csv()
        print(df.describe())

    def value_counts(self) -> None:
        df = self.finance_service.fetch_top_five_tickets()
        df.columns = ["_".join(col).strip() for col in df.columns.values]
        print(df["MSFT_Open"].value_counts())

    def loc(self) -> None:
        df = self.read_csv()
        df.set_index("Datetime", inplace=True)
        df.index = df.index.tz_localize(None) if getattr(df.index, "tz", None) is not None else df.index
        threshold = pd.Timestamp("2025-10-09 19:31:00")
        filtered = df.loc[df.index > threshold, ["Open"]]
        print(filtered)


if __name__=="__main__":
    my_class = PdCoreConcepts()
    # print(my_class.simple_dict)
    # print(my_class.simple_df)
    # my_class.export_csv()
    # my_class.import_csv()
    # my_class.fetch_realtime_csv()
    # my_class.set_index()
    # print(my_class.simple_df.describe())
    # my_class.describe_data()
    # my_class.value_counts()
    # my_class.fetch_realtime_csv()
    my_class.loc()
