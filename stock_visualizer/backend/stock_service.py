from datetime import datetime, timedelta
from .data_loader import StockDataLoader
from .error_handler import DataFetchError, ValidationError

class StockService:
    def __init__(self):
        self.data_loader = StockDataLoader()
        
    def get_stock_data(self, tickers: list, time_range: str) -> dict:
        """Get stock data for multiple tickers"""
        end_date = datetime.now()
        start_date = self._calculate_start_date(time_range)
        
        stock_data = {}
        for ticker in tickers:
            try:
                data = self.data_loader.fetch_stock_data(ticker, start_date, end_date)
                if not data.empty:
                    stock_data[ticker] = data
            except DataFetchError as e:
                raise e
        return stock_data

    @staticmethod
    def _calculate_start_date(time_range: str) -> datetime:
        """Calculate start date based on time range"""
        range_dict = {
            '1w': 7, '1mo': 30, '3mo': 90, '6mo': 180,
            '1y': 365, '3y': 365*3, '5y': 365*5
        }
        if time_range not in range_dict:
            raise ValidationError(f"Invalid time range: {time_range}")
        return datetime.now() - timedelta(days=range_dict[time_range]) 