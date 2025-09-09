import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import yfinance as yf
from datetime import datetime, timedelta
from packaging.version import Version as LooseVersion


def import_stock_data(stock, start='2010-1-1'):
    # Define a Dataframe for storing your stock data
    Data = pd.DataFrame()

    # Using Yahoo Finance to get stock data
    stock = yf.Ticker(stock)
    Data = stock.history(start=start)

    return Data


def log_returns(Data):

    # Assuming you're interested in the 'Close' prices
    log_returns = np.log(1 + Data['Close'].pct_change())
    log_returns = log_returns[1:]

    return log_returns


def volatility_calc(lr):
    daily_volatility = np.std(lr)
    return daily_volatility


def run_monteCarlo(num_simulations, num_days, last_price, log_return):
    # Calculate daily volatility
    daily_vol = volatility_calc(log_return)

    # Initialize a list to store all simulation results
    all_simulations = []

    for x in range(num_simulations):
        price_series = [last_price]

        for y in range(1, num_days):
            price = price_series[-1] * (1 + np.random.normal(0, daily_vol))
            price_series.append(price)

        all_simulations.append(price_series)

    # Convert the list of simulations into a DataFrame all at once
    simulation_dataframe = pd.DataFrame(all_simulations).transpose()

    return simulation_dataframe
