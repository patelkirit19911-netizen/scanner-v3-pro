import pandas as pd
import requests
from dhanhq import dhanhq

from config import (
    DHAN_CLIENT_ID,
    DHAN_ACCESS_TOKEN,
    CSV_URL
)

dhan = dhanhq(DHAN_CLIENT_ID, DHAN_ACCESS_TOKEN)
def load_scrip_master():
    df = pd.read_csv(CSV_URL)
    return df
def get_nifty_stocks():
    df = load_scrip_master()

    nifty50 = [
        "RELIANCE","HDFCBANK","ICICIBANK","INFY","TCS","LT",
        "SBIN","AXISBANK","BHARTIARTL","ITC","KOTAKBANK",
        "HINDUNILVR","BAJFINANCE","MARUTI","ASIANPAINT",
        "SUNPHARMA","NTPC","TITAN","ULTRACEMCO","M&M",
        "POWERGRID","TATAMOTORS","NESTLEIND","HCLTECH",
        "TECHM","WIPRO","BAJAJFINSV","BAJAJFINANCE","ADANIPORTS",
        "ADANIENT","JSWSTEEL","TATASTEEL","INDUSINDBK",
        "CIPLA","GRASIM","EICHERMOT","ONGC","COALINDIA",
        "HEROMOTOCO","DRREDDY","SHRIRAMFIN","TRENT",
        "BEL","SBILIFE","BRITANNIA","HDFCLIFE","BPCL",
        "APOLLOHOSP","BAJAJ-AUTO","HINDALCO"
    ]

    return df[df["SEM_TRADING_SYMBOL"].isin(nifty50)]
def get_live_quotes(security_ids):
    payload = {
        "NSE_EQ": security_ids
    }
    return dhan.quote_data(payload)


def get_historical_data(security_id, from_date, to_date):
    return dhan.intraday_minute_data(
        security_id=security_id,
        exchange_segment="NSE_EQ",
        instrument_type="EQUITY",
        from_date=from_date,
        to_date=to_date
    )
