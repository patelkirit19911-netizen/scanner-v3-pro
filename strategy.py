def long_signal(df, previous_day_low, nifty_bullish):
    """
    Long signal logic
    """
    pass


def short_signal(df, previous_day_high, nifty_bearish):
    """
    Short signal logic
    """
def short_signal(df, previous_day_high, nifty_bearish):

    last = df.iloc[-1]

    pdh_rejection = (
        last["high"] >= previous_day_high and
        last["close"] < previous_day_high
    )

    if not pdh_rejection:
        return None

    return {
        "signal": "SHORT"
    }   
