#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import Holt

API_KEY = "x"
STOCK_SYMBOL = "AAPL"
API_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_SYMBOL}&apikey={API_KEY}"

response = requests.get(API_URL)
data = response.json()

if "Time Series (Daily)" in data:
    time_series = data["Time Series (Daily)"]
    processed_data = [
        {"date": date, "close": float(info["4. close"])}
        for date, info in time_series.items()
    ]
    with open("data.json", "w") as file:
        json.dump(processed_data, file, indent=4)
    print("Stock data saved to data.json")
else:
    print("Error fetching data:", data.get("Note", "Unknown error"))
    exit()

with open("data.json", "r") as file:
    processed_data = json.load(file)

df = pd.DataFrame(processed_data)
df['date'] = pd.to_datetime(df['date'])
df.sort_values("date", inplace=True)
df.reset_index(drop=True, inplace=True)

df['date_ordinal'] = df['date'].map(datetime.datetime.toordinal)

degree = 3
coeffs = np.polyfit(df['date_ordinal'], df['close'], degree)
poly_func = np.poly1d(coeffs)

poly_deriv = np.polyder(poly_func)

holt_model = Holt(df['close'], initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2)

last_date = df['date'].iloc[-1]
future_end_date = last_date + pd.DateOffset(months=2)

all_dates = pd.date_range(start=df['date'].min(), end=future_end_date)
all_ordinals = np.array([date.toordinal() for date in all_dates])

poly_predictions = poly_func(all_ordinals)

holt_fitted = holt_model.fittedvalues.values
forecast_horizon = len(all_dates) - len(df)
holt_forecast = holt_model.forecast(forecast_horizon).values
holt_all = np.concatenate([holt_fitted, holt_forecast])

ensemble_predictions = (poly_predictions + holt_all) / 2

deriv_values = poly_deriv(all_ordinals)

plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['close'], label="Historical Prices", color='blue')
plt.plot(all_dates, poly_predictions, label="Cubic Polynomial Prediction", linestyle='--', color='green')
plt.plot(all_dates, holt_all, label="Holt's Trend Prediction", linestyle='--', color='orange')
plt.plot(all_dates, ensemble_predictions, label="Ensemble Prediction", linestyle='-', color='red', linewidth=2)
plt.xlabel("Date")
plt.ylabel("Closing Price ($)")
plt.title("AAPL Stock Price Trend Prediction (Next Two Months)\n(Combined Methods: Polynomial & Holt's Model)")
plt.legend()
plt.show()

weekly_dates = pd.date_range(start=last_date + datetime.timedelta(days=1), end=future_end_date, freq='W')
weekly_ordinals = np.array([date.toordinal() for date in weekly_dates])
weekly_poly = poly_func(weekly_ordinals)
weekly_holt = holt_model.forecast(len(weekly_dates)).values
weekly_ensemble = (weekly_poly + weekly_holt) / 2
weekly_slopes = poly_deriv(weekly_ordinals)

print("\nWeekly Ensemble Forecast with Slope (Derivative) Insights:")
for date, price, slope in zip(weekly_dates, weekly_ensemble, weekly_slopes):
    print(f"{date.strftime('%Y-%m-%d')}: Predicted Price = ${price:.2f}, Slope = {slope:.4f}")
