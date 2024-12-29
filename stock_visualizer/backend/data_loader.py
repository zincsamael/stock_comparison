import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

class StockDataLoader:
    @staticmethod
    def fetch_stock_data(ticker: str, start_date: datetime, end_date: datetime) -> pd.DataFrame:
        """Fetch stock data for a given ticker and date range"""
        try:
            stock = yf.Ticker(ticker)
            return stock.history(start=start_date, end=end_date)
        except Exception as e:
            raise DataFetchError(f"Error fetching data for {ticker}: {str(e)}")

    @staticmethod
    def get_stock_info(ticker: str) -> dict:
        """Get basic information about a stock"""
        try:
            stock = yf.Ticker(ticker)
            return stock.info
        except Exception as e:
            raise DataFetchError(f"Error fetching info for {ticker}: {str(e)}") 