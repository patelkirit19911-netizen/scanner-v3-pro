def long_signal(df, previous_day_low, nifty_bullish):
    """
    Long signal logic
    """
    pass


def short_signal(df, previous_day_high, nifty_bearish):
    """
    Short signal logic
    """

    last = df.iloc[-1]

    # PDH Rejection
    pdh_rejection = (
        last["high"] >= previous_day_high and
        last["close"] < previous_day_high
    )

    if not pdh_rejection:
        return None

    # Red Candle
    red_candle = last["close"] < last["open"]

    if not red_candle:
    return None

    # VWAP Filter
    below_vwap = last["close"] < last["vwap"]

    if not below_vwap:
        return None

    return {
    "signal": "SHORT"
    }
