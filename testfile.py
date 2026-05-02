import yfinance as yf
import pandas as pd
import numpy as np

# ======================
# PARAMETERS
# ======================
TICKER = "ES=F"
INTERVAL = "5m"
PERIOD = "30d"

SMA_PERIOD = 50
ADX_PERIOD = 14
ATR_PERIOD = 14

ADX_THRESHOLD = 20
DIST_THRESHOLD = -0.01   # -1% below SMA

ATR_STOP_MULT = 2
ATR_TP_MULT = 1.5

MAX_HOLD = 20

# ======================
# LOAD DATA
# ======================
data = yf.download(TICKER, interval=INTERVAL, period=PERIOD)
data = data.dropna()

# FIX MultiIndex
data.columns = data.columns.get_level_values(0)

# ======================
# INDICATORS
# ======================

# SMA
data["SMA"] = data["Close"].rolling(SMA_PERIOD).mean()

# ATR
high_low = data["High"] - data["Low"]
high_close = np.abs(data["High"] - data["Close"].shift())
low_close = np.abs(data["Low"] - data["Close"].shift())

tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
data["ATR"] = tr.rolling(ATR_PERIOD).mean()

# ADX (упрощённая версия)
plus_dm = data["High"].diff()
minus_dm = data["Low"].diff() * -1

plus_dm[plus_dm < 0] = 0
minus_dm[minus_dm < 0] = 0

tr_smooth = tr.rolling(ADX_PERIOD).mean()
plus_di = 100 * (plus_dm.rolling(ADX_PERIOD).mean() / tr_smooth)
minus_di = 100 * (minus_dm.rolling(ADX_PERIOD).mean() / tr_smooth)

dx = (abs(plus_di - minus_di) / (plus_di + minus_di)) * 100
data["ADX"] = dx.rolling(ADX_PERIOD).mean()

# Distance from SMA
data["dist"] = (data["Close"] - data["SMA"]) / data["SMA"]

data = data.dropna()

# ======================
# BACKTEST
# ======================

trades = []

i = 0
while i < len(data) - 1:

    row = data.iloc[i]

    # ===== REGIME: MEAN REVERSION ONLY =====
    if row["ADX"] < ADX_THRESHOLD and row["dist"] < DIST_THRESHOLD:

        entry_price = data.iloc[i + 1]["Open"]
        atr = row["ATR"]

        stop = entry_price - ATR_STOP_MULT * atr
        take = entry_price + ATR_TP_MULT * atr

        exit_price = None
        exit_index = None

        for j in range(i + 1, min(i + 1 + MAX_HOLD, len(data))):
            price = data.iloc[j]["Close"]

            # exit to mean
            if price >= data.iloc[j]["SMA"]:
                exit_price = price
                exit_index = j
                break

            # stop loss
            if price <= stop:
                exit_price = price
                exit_index = j
                break

            # take profit
            if price >= take:
                exit_price = price
                exit_index = j
                break

        if exit_price is None:
            exit_index = min(i + 1 + MAX_HOLD, len(data) - 1)
            exit_price = data.iloc[exit_index]["Close"]

        profit = (exit_price - entry_price) / entry_price
        trades.append(profit)

        i = exit_index
    else:
        i += 1

# ======================
# RESULTS
# ======================

trades = np.array(trades)

if len(trades) > 0:
    print(f"Trades: {len(trades)}")
    print(f"Avg Return: {trades.mean()}")
    print(f"Win Rate: {(trades > 0).mean()}")
    print(f"Total Return: {trades.sum()}")
else:
    print("No trades")