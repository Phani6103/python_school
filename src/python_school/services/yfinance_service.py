"""
Utilities for retrieving market data using the yfinance library.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Final, Optional

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
        normalized = frame.reset_index()
        self.current_frame = normalized
        return normalized
    
    def save_file(self, symbol: str, frame: Optional[pd.DataFrame] = None, *, directory: Optional[Path] = None) -> Path:
        output_path = (directory or Path.cwd() / "test_data") / f"{symbol.upper()}.csv"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        data = frame if frame is not None else self.current_frame
        if data.empty:
            raise ValueError("No market data available to save; fetch data before calling save_file.")
        data.to_csv(output_path, index=False)
        return output_path
    
    def fetch_top_five_tickets(self):
        # symbols = ['MSFT', 'AAPL', 'NVDA', 'GOOGL', 'AMZN']
        # data = {}
        # for symbol in symbols:
        #     try:
        #         df = self.fetch_ticker(symbol, period="1d", interval="1m")
        #         data[symbol] = df
        #     except ValueError as e:
        #         print(f"Could not fetch data for {symbol}: {e}")
        # return data
        # call the api to get the stocks data of all 5 tickets at a time
        symbols = ['MSFT', 'AAPL', 'NVDA', 'GOOGL', 'AMZN']
        data = yf.download(
            tickers=" ".join(symbols),
            period="1d",
            interval="1m",
            group_by='ticker',
            progress=False,
            auto_adjust=True,
        )
        
        # # To get the 'Close' price for each ticker
        # close_prices = pd.DataFrame({symbol: data[symbol]['Close'] for symbol in symbols})
        
        # # Count the occurrences of each unique close price
        # value_counts_df = close_prices.apply(pd.Series.value_counts).fillna(0)
        # return value_counts_df
        return data
        
        
