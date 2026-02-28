import pandas as pd

def run_backtest(
    prices: pd.DataFrame,
    signals: pd.Series,
    transaction_cost: float = 0.0005,
) -> pd.Series:
    """
    Run a simple backtest with transaction costs.
    """
    returns = prices["close"].pct_change()

    # Avoid lookahead bias
    positions = signals.shift(1).fillna(0)

    pnl = positions * returns
    pnl -= transaction_cost * positions.diff().abs()

    return pnl.dropna()