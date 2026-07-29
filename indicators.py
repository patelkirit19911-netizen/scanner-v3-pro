import pandas as pd
from ta.volatility import AverageTrueRange
def calculate_vwap(df):
    df = df.copy()
    tp = (df["high"] + df["low"] + df["close"]) / 3
    df["vwap"] = (tp * df["volume"]).cumsum() / df["volume"].cumsum()
    return df
