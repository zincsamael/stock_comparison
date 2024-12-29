import streamlit as st

class Controls:
    @staticmethod
    def create_time_range_selector():
        return st.selectbox(
            "Time range",
            ['1w', '1mo', '3mo', '6mo', '1y', '3y', '5y'],
            index=4
        )

    @staticmethod
    def create_reset_button():
        return st.button("Reset View") 