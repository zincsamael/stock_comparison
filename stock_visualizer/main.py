from stock_plotter import plot_stock_comparison

def main():
    # Example usage with META and GOOGL
    # tickers = ['META', 'GOOGL']
    # plot_stock_comparison(tickers)
    
    # Example with specific date range
    # plot_stock_comparison(
    #     tickers=['META', 'GOOGL'], 
    #     start_date='2023-01-01', 
    #     end_date='2024-01-01'
    # )
    
    # Example with more stocks
    tickers = ['META', 'GOOGL', 'AAPL', 'MSFT', 'AMZN']
    plot_stock_comparison(tickers, time_range='1y')

if __name__ == "__main__":
    main()
