from setuptools import setup, find_packages

setup(
    name="stock_visualizer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'yfinance',
        'plotly',
        'pandas'
    ],
) 