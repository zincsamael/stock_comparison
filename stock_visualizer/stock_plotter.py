import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

def get_stock_data(tickers, time_range):
    """
    Fetch stock data for given tickers and time range
    
    Parameters:
    tickers (list): List of stock ticker symbols
    time_range (str): Time range (1w, 1mo, 3mo, 6mo, 1y, 3y, 5y)
    """
    end_date = datetime.now()
    
    # Define time ranges
    range_dict = {
        '1w': timedelta(days=7),
        '1mo': timedelta(days=30),
        '3mo': timedelta(days=90),
        '6mo': timedelta(days=180),
        '1y': timedelta(days=365),
        '3y': timedelta(days=3*365),
        '5y': timedelta(days=5*365)
    }
    
    start_date = end_date - range_dict[time_range]
    
    data = {}
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(start=start_date, end=end_date)
            if not hist.empty:
                data[ticker] = hist
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    
    return data

def create_stock_figure(stock_data):
    """
    Create an interactive plot using plotly
    """
    fig = go.Figure()
    
    for ticker, data in stock_data.items():
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data['Close'],
                name=ticker,
                mode='lines',
                hovertemplate=
                "<b>%{x}</b><br>" +
                "Price: $%{y:.2f}<br>" +
                "<extra></extra>"
            )
        )
    
    fig.update_layout(
        title='Stock Price Comparison',
        xaxis_title='Date',
        yaxis_title='Stock Price (USD)',
        hovermode='x unified',
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        template="plotly_white"  # Clean white template
    )
    
    # Add range selector buttons
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=7, label="1w", step="day", stepmode="backward"),
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=3, label="3m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(count=3, label="3y", step="year", stepmode="backward"),
                dict(count=5, label="5y", step="year", stepmode="backward"),
                dict(step="all", label="Max")
            ])
        )
    )
    
    return fig

def plot_stock_comparison(tickers, time_range='1y'):
    """
    Main function to create and display the interactive stock comparison plot
    
    Parameters:
    tickers (list): List of stock ticker symbols
    time_range (str): Time range (1w, 1mo, 3mo, 6mo, 1y, 3y, 5y)
    """
    stock_data = get_stock_data(tickers, time_range)
    fig = create_stock_figure(stock_data)
    fig.show()
