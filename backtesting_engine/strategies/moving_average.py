import pandas as pd

class MovingAverageStrategy:
    def __init__(self, short_window: int, long_window: int):
        if short_window >= long_window:
            raise ValueError("short_window must be < long_window")

        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, prices: pd.DataFrame) -> pd.Series:
        """
        Generate long-only signals:
        1 = long
        0 = flat
        """
        signals = pd.Series(0, index=prices.index)

        short_ma = prices["close"].rolling(self.short_window).mean()
        long_ma = prices["close"].rolling(self.long_window).mean()

        signals[short_ma > long_ma] = 1
        return signals