import pandas as pd
import requests
from dhanhq import dhanhq

from config import (
    DHAN_CLIENT_ID,
    DHAN_ACCESS_TOKEN,
    CSV_URL
)

dhan = dhanhq(DHAN_CLIENT_ID, DHAN_ACCESS_TOKEN)
