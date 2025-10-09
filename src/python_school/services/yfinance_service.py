"""
Utilities for retrieving market data using the yfinance library.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final
from pathlib import Path

import pandas as pd
import yfinance as yf


@dataclass(frozen=True)
class YFinanceRequest:
    """Request parameters controlling how ticker data is fetched."""

    symbol: str
    period: str = "1d"
    interval: str = "1m"


class YFinanceService:
    """Light wrapper around yfinance helpers to keep API usage centralized."""

    _DEFAULT_PERIOD: Final[str] = "1d"
    _DEFAULT_INTERVAL: Final[str] = "1m"
    current_frame = pd.DataFrame()

    def fetch_ticker(self, symbol: str, period: str | None = None, interval: str | None = None) -> pd.DataFrame:
        """Return a DataFrame of ticker data for the requested window.

        Raises:
            ValueError: If yfinance returns an empty frame (usually outside trading hours).
        """
        params = YFinanceRequest(
            symbol=symbol,
            period=period or self._DEFAULT_PERIOD,
            interval=interval or self._DEFAULT_INTERVAL,
        )
        frame = yf.download(
            tickers=params.symbol,
            period=params.period,
            interval=params.interval,
            progress=False,
            auto_adjust=True,
        )
        if frame.empty:
            raise ValueError(f"No data returned for {params.symbol} with period={params.period} interval={params.interval}.")
        self.current_frame = frame
        return frame.reset_index()
    
    def save_file(self, symbol: str):
        output_path = Path.cwd() / "test_data" / f"{symbol}.csv"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        self.current_frame.to_csv(output_path, index=False)
        print("File saved successfully to: ", output_path)
        
