import pandas as pd
from ta.volatility import AverageTrueRange
def calculate_vwap(df):
    df = df.copy()
    tp = (df["high"] + df["low"] + df["close"]) / 3
    df["vwap"] = (tp * df["volume"]).cumsum() / df["volume"].cumsum()
    return df

def calculate_rvol(df, period=20):
    df = df.copy()
    df["avg_volume"] = df["volume"].rolling(period).mean()
    df["rvol"] = df["volume"] / df["avg_volume"]
    return df
def calculate_atr(df, period=14):
    atr = AverageTrueRange(
        high=df["high"],
        low=df["low"],
        close=df["close"],
        window=period
    )
    df["atr"] = atr.average_true_range()
    return df
