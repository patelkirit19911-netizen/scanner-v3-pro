import pandas as pd
import requests
from dhanhq import dhanhq, DhanContext

from config import (
    DHAN_CLIENT_ID,
    DHAN_ACCESS_TOKEN,
    CSV_URL
)

dhan_context = DhanContext(DHAN_CLIENT_ID, DHAN_ACCESS_TOKEN)
dhan = dhanhq(dhan_context)
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
    url = "https://api.dhan.co/v2/marketfeed/quote"

    headers = {
        "access-token": DHAN_ACCESS_TOKEN,
        "client-id": DHAN_CLIENT_ID,
        "Content-Type": "application/json"
    }

    payload = {
        "NSE_EQ": security_ids
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()


def get_historical_data(security_id, from_date, to_date):
    return dhan.intraday_minute_data(
        security_id=security_id,
        exchange_segment="NSE_EQ",
        instrument_type="EQUITY",
        from_date=from_date,
        to_date=to_date
    )
