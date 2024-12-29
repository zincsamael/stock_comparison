import streamlit as st
from stock_visualizer.backend.stock_service import StockService

class TickerInput:
    @staticmethod
    def create_ticker_input():
        return st.text_input(
            "Enter stock symbols (comma-separated)",
            "META,GOOGL",
            help="Example: AAPL,MSFT,GOOGL"
        )

    @staticmethod
    def parse_tickers(input_string: str) -> list:
        return [ticker.strip().upper() for ticker in input_string.split(',')] 