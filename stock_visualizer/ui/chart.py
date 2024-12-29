import plotly.graph_objects as go

class StockChart:
    @staticmethod
    def create_figure(stock_data: dict, tickers: list):
        fig = go.Figure()
        
        # Add traces
        for ticker in tickers:
            if ticker in stock_data:
                hist = stock_data[ticker]
                if not hist.empty:
                    fig.add_trace(
                        go.Scatter(
                            x=hist.index,
                            y=hist['Close'],
                            name=ticker,
                            mode='lines',
                            hovertemplate=
                            "<b>%{x}</b><br>" +
                            ticker + ": $%{y:.2f}<br>" +
                            "<extra></extra>"
                        )
                    )

        # Configure layout
        fig.update_layout(
            title={
                'text': 'Stock Price Comparison',
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            xaxis_title='Date',
            yaxis_title='Price (USD)',
            hovermode='x unified',
            template='plotly_white',
            height=600,
            xaxis=dict(
                rangeslider=dict(visible=False),
                showspikes=True
            ),
            dragmode='pan'
        )

        config = {
            'scrollZoom': True,
            'displayModeBar': False,
            'doubleClick': False,
            'showTips': False,
            'displaylogo': False,
        }

        return fig, config 