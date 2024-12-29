import streamlit as st

class StockDisplay:
    @staticmethod
    def show_summary_statistics(stock_data: dict):
        st.subheader("📊 Summary Statistics")
        cols = st.columns(len(stock_data))
        
        for idx, (ticker, data) in enumerate(stock_data.items()):
            with cols[idx]:
                current_price = data['Close'][-1]
                start_price = data['Close'][0]
                price_change = ((current_price - start_price) / start_price) * 100
                
                st.metric(
                    f"{ticker}",
                    f"${current_price:.2f}",
                    f"{price_change:.1f}%"
                ) 