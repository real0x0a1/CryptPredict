#!/usr/bin/python3

# -*- Author: Ali (Real0x0a1) -*-
# -*- Description: Predict cryptocurrency prices using linear regression. -*-

import ccxt
import numpy as np
from sklearn.linear_model import LinearRegression as lr
from sklearn.model_selection import train_test_split as tts
import datetime


def fetch_historical_data(exchange, symbol, start_date):
    try:
        since = exchange.parse8601(start_date)
        ohlcvs = exchange.fetch_ohlcv(symbol, '1d', since=since)
        return np.array(ohlcvs)
    except ccxt.NetworkError as e:
        print(f"NetworkError: {e}")
    except ccxt.ExchangeError as e:
        print(f"ExchangeError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def prepare_data(ohlcvs):
    X = np.arange(len(ohlcvs)).reshape(-1, 1)
    y = ohlcvs[:, 4]  # Closing prices
    return X, y


def split_data(X, y, test_size=0.2, random_state=42):
    return tts(X, y, test_size=test_size, random_state=random_state)


def train_linear_regression_model(X_train, y_train):
    model = lr()
    model.fit(X_train, y_train)
    return model


def make_predictions(model, last_date, future_days):
    next_dates = np.arange(last_date + 1, last_date + 1 + future_days).reshape(-1, 1)
    predicted_prices = model.predict(next_dates)
    return predicted_prices


def display_predictions(ohlcvs, predicted_prices, future_days):
    for i in range(future_days):
        date = datetime.datetime.utcfromtimestamp(ohlcvs[-1][0] / 1000) + datetime.timedelta(days=i)
        price = predicted_prices[i]
        print(f"{date}: Predicted Price: {price:.2f} USDT")


def main():
    try:
        # Define the cryptocurrency symbol you want to predict (e.g., Bitcoin)
        symbol = 'BTC/USDT'

        # Initialize the exchange
        exchange = ccxt.binance()  # You can change the exchange as needed

        # Fetch historical data
        start_date = '2023-01-01T00:00:00Z'
        ohlcvs = fetch_historical_data(exchange, symbol, start_date)

        # Prepare the data
        X, y = prepare_data(ohlcvs)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = split_data(X, y)

        # Create and train a linear regression model
        model = train_linear_regression_model(X_train, y_train)

        # Make predictions
        future_days = 7  # Number of days to predict into the future
        last_date = X[-1][0]
        predicted_prices = make_predictions(model, last_date, future_days)

        # Display the predicted prices
        display_predictions(ohlcvs, predicted_prices, future_days)
    except ccxt.NetworkError as e:
        print(f"NetworkError: {e}")
    except ccxt.ExchangeError as e:
        print(f"ExchangeError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
