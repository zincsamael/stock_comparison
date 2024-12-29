import streamlit as st
from ui.chart import StockChart
from ui.controls import Controls
from ui.ticker_input import TickerInput
from ui.display import StockDisplay
from backend.stock_service import StockService
from backend.error_handler import handle_error

def main():
    st.set_page_config(page_title="Stock Visualizer", page_icon="📈", layout="wide")
    st.title("📈 Interactive Stock Visualizer")

    # Initialize services
    stock_service = StockService()

    try:
        # Get user inputs
        col1, col2 = st.columns([2, 1])
        with col1:
            ticker_input = TickerInput.create_ticker_input()
        with col2:
            time_range = Controls.create_time_range_selector()

        # Process inputs
        tickers = TickerInput.parse_tickers(ticker_input)
        
        # Fetch data
        stock_data = stock_service.get_stock_data(tickers, time_range)

        # Create and display chart
        if stock_data:
            fig, config = StockChart.create_figure(stock_data, tickers)
            
            # Add reset button
            if Controls.create_reset_button():
                st.experimental_rerun()
            
            # Display chart
            st.plotly_chart(fig, use_container_width=True, config=config)

            # Display statistics
            StockDisplay.show_summary_statistics(stock_data)

        # Add footer
        st.markdown("---")
        st.markdown("Data provided by Yahoo Finance")

    except Exception as e:
        st.error(handle_error(e))

if __name__ == "__main__":
    main() 