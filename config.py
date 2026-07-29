import os

DHAN_CLIENT_ID = os.getenv("DHAN_CLIENT_ID")
DHAN_ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN")

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

CSV_URL = "https://images.dhan.co/api-data/api-scrip-master.csv"

# Scanner Settings
TIMEFRAME = "5"
RVOL_THRESHOLD = 2.0
ATR_PERIOD = 14
RISK_REWARD_1 = 1
RISK_REWARD_2 = 2
