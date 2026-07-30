def buy_signal(candle, previous_day_high, rvol):
    if (
        candle["high"] >= previous_day_high and
        candle["close"] > previous_day_high and
        candle["close"] > candle["open"] and
        rvol >= 2.0
    ):
        return True
    return False


def sell_signal(candle, previous_day_high, rvol):
    if (
        candle["high"] >= previous_day_high and
        candle["close"] < previous_day_high and
        candle["close"] < candle["open"] and
        rvol >= 2.0
    ):
        return True
    return False
