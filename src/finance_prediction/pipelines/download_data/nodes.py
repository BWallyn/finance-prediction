"""
This is a boilerplate pipeline 'download_data'
generated using Kedro 0.19.8
"""
# =================
# ==== IMPORTS ====
# =================

import datetime
import os

import pandas as pd
import yfinance as yf

# ===================
# ==== FUNCTIONS ====
# ===================

def download_data_today(symbol: str) -> pd.DataFrame:
    """Download data of the day

    Args:
        symbol (str): Symbol of the finance on Yahoo Finance
    Returns:
        target_data (pd.DataFrame): Data of the finance index value
    """
    # Symbol on Yahoo Finance
    target_symbol = symbol
    # Define date
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    # Download historical data
    try:
        target_data = yf.download(target_symbol, start=today, end=None)
        target_data.reset_index(inplace=True)
        target_data['Date'] = target_data['Date'].dt.strftime('%Y-%m-%d')
        target_data['Date'] = pd.to_datetime(target_data['Date'])
        target_data = target_data[['Date', 'Close']]
    except Exception:
        target_data = pd.DataFrame()
    return target_data


def download_data_period(symbol: str, date_start: str, date_end: str) -> pd.DataFrame:
    """Download data on a specific period

    Args:
        symbol (str): Symbol of the finance on Yahoo Finance
        date_start (str): Start date of the period
        end_date (str): End date of the period
    Returns:
        target_data (pd.DataFrame): Data of the finance index value
    """
    # Symbol on Yahoo Finance
    target_symbol = symbol
    # Define date
    format_string = "%Y-%m-%d"
    date_start = datetime.strptime(date_start, format_string)
    date_end = datetime.strptime(date_end, format_string)

    # Download historical data
    try:
        target_data = yf.download(target_symbol, start=date_start, end=date_end)
        target_data.reset_index(inplace=True)
        target_data['Date'] = target_data['Date'].dt.strftime('%Y-%m-%d')
        target_data['Date'] = pd.to_datetime(target_data['Date'])
        target_data = target_data[['Date', 'Close']]
    except Exception:
        target_data = pd.DataFrame()
    return target_data


def save_data(df: pd.DataFrame, symbol: str, path_data: str) -> None:
    """Save data to the dataset if not already present in the dataset

    Args:
        df (pd.DataFrame): Input dataframe
        symbol (str): Symbol of the finance index on Yahoo finance
        path_data (str): Path to the data folder
    """
    if not df.empty:
        # Load historic data
        hist_file_name = os.path.join(path_data, f'{symbol}.csv')
        df_hist = pd.read_csv(hist_file_name)
        # Convert the date column to the right type
        df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

        # Check if the last date in the history data is the same as the date of the data downloaded
        if df_hist['Date'].iloc[-1] == df['Date'].iloc[0]:
            # TODO log info to logger
            pass
        else:
            df = pd.concat([df, df_hist])

            # Save the updated dataframe
            df.to_csv(hist_file_name, index=False)
